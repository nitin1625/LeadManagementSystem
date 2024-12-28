from rest_framework import serializers
from .models import  Order
from leads.models import Restaurant

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'lead_status', 'potential_revenue', 'cuisine_type', 'restaurant_type']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['restaurant', 'order_date', 'amount']
