from django.urls import path
from .views import InsurancePolicyCreateView


urlpatterns = [
    path('api/custom-person-create/', InsurancePolicyCreateView.as_view(), name='custom-person-create'),
]
