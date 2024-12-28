# interaction_tracking/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InteractionViewSet

router = DefaultRouter()
router.register(r'interactions', InteractionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
