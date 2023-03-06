# Django
from django.urls import path

# Libraries
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("/login", TokenObtainPairView.as_view(), name="token_generation"),
    path("/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
