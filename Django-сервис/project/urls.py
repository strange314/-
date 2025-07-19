from django.urls import path
from .views import generate_token, secret_data

urlpatterns = [
    path('api/gen-token/', generate_token),
    path('api/secret-data/', secret_data),
]
