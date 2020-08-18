from django.urls import path, include
from rest_framework import routers
from apps.tokens.api import views

token_router = routers.DefaultRouter()

token_router.register(r'tokens', views.TokenView)


urlpatterns = [
    path('device-info/', include(token_router.urls)),
]