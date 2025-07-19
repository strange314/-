from django.urls import path
from .views import SecretDataView
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('api/gen-token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/secret-data/', SecretDataView.as_view(), name='secret_data'),
]
