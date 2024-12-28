from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Restaurant, Order
from .serializers import RestaurantSerializer
from django.db.models import Sum, Count
from datetime import timedelta
from django.utils import timezone


class PerformingAccountsView(APIView):
    """
    Fetch all restaurant accounts that are performing well based on their lead status and potential revenue.
    """
    def get(self, request):
        # Fetch well-performing accounts (e.g., those with a 'CONVERTED' status and potential revenue >= 10000)
        accounts = Restaurant.objects.filter(lead_status='CONVERTED', potential_revenue__gte=10000)
        serializer = RestaurantSerializer(accounts, many=True)
        return Response(serializer.data)


class OrderPatternsView(APIView):
    """
    Fetch data regarding ordering frequency, including last month's and this month's orders.
    """
    def get(self, request):
        # Get the current date and calculate the first and last day of the current and last months
        today = timezone.now()
        first_day_this_month = today.replace(day=1)
        first_day_last_month = (today.replace(day=1) - timedelta(days=1)).replace(day=1)
        last_day_last_month = today.replace(day=1) - timedelta(days=1)
        
        order_data = []
        restaurants = Restaurant.objects.all()

        for restaurant in restaurants:
            orders_last_month = Order.objects.filter(
                restaurant=restaurant,
                order_date__gte=first_day_last_month,
                order_date__lte=last_day_last_month
            ).count()

            orders_this_month = Order.objects.filter(
                restaurant=restaurant,
                order_date__gte=first_day_this_month
            ).count()

            order_data.append({
                "restaurant_id": restaurant.id,
                "name": restaurant.name,
                "orders_last_month": orders_last_month,
                "orders_this_month": orders_this_month
            })

        return Response(order_data)


class UnderperformingAccountsView(APIView):
    """
    Identify underperforming accounts based on lead status and revenue.
    """
    def get(self, request):
        # Identify underperforming accounts (e.g., with 'NEW' or 'LOST' status and low revenue)
        underperforming = Restaurant.objects.filter(lead_status__in=['NEW', 'LOST'], potential_revenue__lte=10000)
        serializer = RestaurantSerializer(underperforming, many=True)
        return Response(serializer.data)
