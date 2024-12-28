from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Interaction
from .serializers import InteractionSerializer

class InteractionViewSet(viewsets.ModelViewSet):

    queryset = Interaction.objects.all()
    serializer_class = InteractionSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

    def list(self, request, *args, **kwargs):
        queryset = Interaction.objects.all()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def orders(self, request):
        queryset = self.get_queryset().filter(order_placed=True)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):

        interaction = self.get_object()
        serializer = self.get_serializer(interaction)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):

        interaction = self.get_object()
        serializer = self.get_serializer(interaction, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        interaction = self.get_object()
        interaction.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
