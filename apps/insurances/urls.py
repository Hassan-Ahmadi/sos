from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PersonModelViewSet, InsurancePolicyCreateView


# router = DefaultRouter()
# router.register(r'persons', PersonModelViewSet, basename='person')
# router.register(r'insurance-companies', InsuranceCompanyViewSet, basename='insurance-company')
# router.register(r'policyholders', PolicyholderViewSet, basename='policyholder')
# router.register(r'insurance-policies', InsurancePolicyViewSet, basename='insurance-policy')
# router.register(r'insurance-plans', InsurancePlanViewSet, basename='insurance-plan')


urlpatterns = [
    # path('', include(router.urls)),  # All API endpoints
    path('api/custom-person-create/', InsurancePolicyCreateView.as_view(), name='custom-person-create'),
]
