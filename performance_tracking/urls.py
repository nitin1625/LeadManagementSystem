from django.urls import path
from .views import PerformingAccountsView, OrderPatternsView, UnderperformingAccountsView

urlpatterns = [
    path('well/', PerformingAccountsView.as_view(), name='performing-accounts'),
    path('order_patterns/', OrderPatternsView.as_view(), name='order-patterns'),
    path('under/', UnderperformingAccountsView.as_view(), name='underperforming-accounts')
]
