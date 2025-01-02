from rest_framework import serializers
from .models import Interaction , Order
from leads.models import Restaurant  # Lead model
from contact.models import Contact  # Contact model


class InteractionSerializer(serializers.ModelSerializer):
    # Ensure valid relationships by using `PrimaryKeyRelatedField`
    lead = serializers.PrimaryKeyRelatedField(queryset=Restaurant.objects.all())
    contact = serializers.PrimaryKeyRelatedField(queryset=Contact.objects.all())

    class Meta:
        model = Interaction
        fields = ['id', 'lead', 'contact', 'interaction_type', 'details', 'order_placed', 'date']

class OrderSerializer(serializers.ModelSerializer):
    restaurant= serializers.PrimaryKeyRelatedField(queryset=Restaurant.objects.all())
    class Meta:
        model = Order
        fields = [
            'id', 
            'restaurant', 
            'order_date', 
            'amount',
           
        ]
       