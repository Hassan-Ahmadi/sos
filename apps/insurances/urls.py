from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PersonViewSet, InsuranceCompanyViewSet, PolicyholderViewSet, InsurancePolicyViewSet, InsurancePlanViewSet

router = DefaultRouter()
router.register(r'persons', PersonViewSet, basename='person')
router.register(r'insurance-companies', InsuranceCompanyViewSet, basename='insurance-company')
router.register(r'policyholders', PolicyholderViewSet, basename='policyholder')
router.register(r'insurance-policies', InsurancePolicyViewSet, basename='insurance-policy')
router.register(r'insurance-plans', InsurancePlanViewSet, basename='insurance-plan')

urlpatterns = [
    path('api/', include(router.urls)),  # All API endpoints
]