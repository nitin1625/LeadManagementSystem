from rest_framework.routers import DefaultRouter
from .views import CallPlanViewSet
from django.urls import path, include

router = DefaultRouter()
router.register('', CallPlanViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
