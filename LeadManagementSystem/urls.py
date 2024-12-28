from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('lead/', include('leads.urls')),
    path('contact/', include('contact.urls')),
    path('track/', include('interaction_tracking.urls')),
    path('call/', include('call_planning.urls')),
    path('performance/', include('performance_tracking.urls')),
]