# interaction_tracking/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'interactions', InteractionViewSet)
router.register(r'orders',OrderViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
