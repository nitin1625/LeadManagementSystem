from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from django.core.exceptions import ValidationError
from .models import *
from .serializers import RestaurantSerializer
from .permissions import IsKAMOrAdmin
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework.views import APIView
from django.http import HttpResponse

class SecuredLeadView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({'message': 'This is a secured endpoint!'})
    
class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [IsAuthenticated, IsKAMOrAdmin]

    def get_queryset(self):
        """
        Filter leads to show only those assigned to the requesting user,
        unless the user is an admin
        """
        if self.request.user.is_superuser:
            return Restaurant.objects.all()
        return Restaurant.objects.filter(assigned_to=self.request.user)

    def perform_create(self, serializer):
        """Assign the lead to the current user"""
        serializer.save(assigned_to=self.request.user)

    @extend_schema(
        parameters=[
            OpenApiParameter(name='status', description='Filter by lead status', required=False),
        ]
    )
    def list(self, request, *args, **kwargs):
        """List leads with optional status filter"""
        status_filter = request.query_params.get('status', None)
        queryset = self.get_queryset()
        
        if status_filter:
            queryset = queryset.filter(lead_status=status_filter)
        
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def change_status(self, request, pk=None):
        """Custom endpoint to change lead status"""
        lead = self.get_object()
        new_status = request.data.get('status')
        if new_status not in dict(Restaurant.LEAD_STATUS_CHOICES):
            return Response(
                {'error': 'Invalid status'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        LeadStatusHistory.objects.create(
        lead=lead,
        old_status=lead.lead_status,
        new_status=new_status,
        changed_by=request.user
    )
        
        lead.lead_status = new_status
        lead.save()
        return Response(self.get_serializer(lead).data)
    

    @action(detail=True, methods=['get'])
    def status_history(self, request, pk=None):
        """Retrieve the status history of a specific restaurant"""
        restaurant = self.get_object()
        status_history = restaurant.status_history.all() 
        history_data = [
            {
                'old_status': history.old_status,
                'new_status': history.new_status,
                'changed_by': history.changed_by.username,
                'changed_at': history.changed_at
            }
            for history in status_history
        ]
        return Response(history_data)

