from rest_framework import serializers
from .models import Interaction
from leads.models import Restaurant  # Lead model
from contact.models import Contact  # Contact model


class InteractionSerializer(serializers.ModelSerializer):
    # Ensure valid relationships by using `PrimaryKeyRelatedField`
    lead = serializers.PrimaryKeyRelatedField(queryset=Restaurant.objects.all())
    contact = serializers.PrimaryKeyRelatedField(queryset=Contact.objects.all())

    class Meta:
        model = Interaction
        fields = ['id', 'lead', 'contact', 'interaction_type', 'details', 'order_placed', 'date']
