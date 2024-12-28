# contact/views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Contact
from .serializers import ContactSerializer
from leads.models import Restaurant  # Adjust the import based on your project structure
class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated]  # Use your custom permission classes if needed

    def perform_create(self, serializer):
        # Ensure the contact is linked to a restaurant on creation
        restaurant = self.request.data.get('restaurant')
        if not Restaurant.objects.filter(id=restaurant).exists():
            raise ValidationError("Invalid restaurant ID")
        serializer.save(restaurant_id=restaurant)
