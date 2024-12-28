from rest_framework import serializers
from .models import CallPlan
from leads.models import Restaurant  # Assuming Restaurant model exists

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'address']  # Add fields you need

class CallPlanSerializer(serializers.ModelSerializer):
    lead = RestaurantSerializer()  # Serialize the related lead

    class Meta:
        model = CallPlan
        fields = ['id', 'lead', 'frequency', 'last_called', 'next_call_date', 'notes']

    def update(self, instance, validated_data):
        """Override update method to handle updates like frequency"""
        instance.frequency = validated_data.get('frequency', instance.frequency)
        instance.save()
        return instance
