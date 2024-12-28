from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from .models import CallPlan
from .serializers import CallPlanSerializer
from rest_framework.permissions import IsAuthenticated
from leads.models import Restaurant
class CallPlanViewSet(viewsets.ModelViewSet):
    queryset = CallPlan.objects.all()
    serializer_class = CallPlanSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):

        frequency = request.data.get('frequency')
        lead_id = request.data.get('lead')  # Assuming you pass the lead ID in the request

        try:
            lead = Restaurant.objects.get(id=lead_id)
        except Restaurant.DoesNotExist:
            return Response({"detail": "Restaurant (Lead) not found."}, status=404)

        if frequency == 'DAILY':
            next_call_date = timezone.now() + timezone.timedelta(days=1)
        elif frequency == 'WEEKLY':
            next_call_date = timezone.now() + timezone.timedelta(weeks=1)
        elif frequency == 'BIWEEKLY':
            next_call_date = timezone.now() + timezone.timedelta(weeks=2)
        elif frequency == 'MONTHLY':
            next_call_date = timezone.now() + timezone.timedelta(days=30)
        else:
            return Response({"detail": "Invalid frequency."}, status=400)

        call_plan = CallPlan.objects.create(
            lead=lead,
            frequency=frequency,
            next_call_date=next_call_date,
            last_called=None,  # No call made yet
            notes=request.data.get('notes', '')
        )

        serializer = self.get_serializer(call_plan)
        return Response(serializer.data, status=201)

    @action(detail=False, methods=['get'])
    def today_calls(self, request):
        """
        Display all leads requiring calls today.
        """
        today = timezone.now().date()
        due_calls = CallPlan.objects.filter(next_call_date__date=today)
        serializer = self.get_serializer(due_calls, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def record_call(self, request, pk=None):
        """
        Track the last call made and update next call date.
        """
        call_plan = self.get_object()
        call_plan.last_called = timezone.now()  # Update the last called time
        call_plan.update_next_call()  # Update the next call date based on frequency
        serializer = self.get_serializer(call_plan)
        return Response(serializer.data)

    @action(detail=True, methods=['patch'])
    def set_frequency(self, request, pk=None):
        """
        Set or update the call frequency for the given lead.
        """
        call_plan = self.get_object()
        frequency = request.data.get('frequency')
        if frequency:
            call_plan.frequency = frequency
            call_plan.save()
            serializer = self.get_serializer(call_plan)
            return Response(serializer.data)
        return Response({"detail": "Frequency not provided."}, status=400)
