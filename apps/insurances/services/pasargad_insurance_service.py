from rest_framework.exceptions import ValidationError

from .base_insurance_service import BaseInsuranceService
from ..models.person import Person
from ..models.insurance_company import InsuranceCompany
from ..models.insurance_plan import InsurancePlan
from ..models.insurance_policy import InsurancePolicy
from ..models.policy_holder import Policyholder
from django.db import transaction
from ..serializers import (PersonSerializer,
                           InsuranceCompanySerializer,
                           PolicyholderSerializer,
                           InsurancePlanSerializer,
                           InsurancePolicySerializer)


class PasargadInsuranceService(BaseInsuranceService):

    def _get_or_create_person(self, person_data: dict) -> Person:
        person_serializer = PersonSerializer(data=person_data)
        if person_serializer.is_valid():
            person, created = Person.objects.get_or_create(**person_serializer.validated_data)
            return person
        else:
            raise ValidationError(person_serializer.errors)

    def _get_or_create_insurance_company(self, insurance_company_data: dict) -> InsuranceCompany:
        insurance_company_serializer = InsuranceCompanySerializer(data=insurance_company_data)
        if insurance_company_serializer.is_valid():
            insurance_company, created = InsuranceCompany.objects.get_or_create(**insurance_company_serializer.validated_data)
            return insurance_company
        else:
            raise ValidationError(insurance_company_serializer.errors)

    def _get_or_create_policy_holder(self, policy_holder_data: dict) -> Policyholder:
        policy_holder_serializer = PolicyholderSerializer(data=policy_holder_data)
        if policy_holder_serializer.is_valid():
            policy_holder, created = Policyholder.objects.get_or_create(**policy_holder_serializer.validated_data)
            return policy_holder
        else:
            raise ValidationError(policy_holder_serializer.errors)

    def _get_or_create_insurance_plan(self, insurance_plan_data: dict) -> InsurancePlan:
        insurance_plan_serializer = InsurancePlanSerializer(data=insurance_plan_data)
        if insurance_plan_serializer.is_valid():
            insurance_plan, created = InsurancePlan.objects.get_or_create(**insurance_plan_serializer.validated_data)
            return insurance_plan
        else:
            raise ValidationError(insurance_plan_serializer.errors)

    def create_insurance_policy(self, data: dict) -> InsurancePolicy:

        try:
            with transaction.atomic():
                person = self._get_or_create_person(person_data=data.get('person'))
                insurance_company = self._get_or_create_insurance_company(insurance_company_data=data.get('insurance_company'))
                policy_holder = self._get_or_create_policy_holder(policy_holder_data=data.get('policyholder'))
                insurance_plan = self._get_or_create_insurance_plan(insurance_plan_data=data.get('insurance_plan'))

                insurance_policy_serializer = InsurancePolicySerializer(data=data.get('insurance_policy'))
                if insurance_policy_serializer.is_valid():
                    insurance_policy = InsurancePolicy.objects.create(person=person,
                                                                      insurance_company=insurance_company,
                                                                      policyholder=policy_holder,
                                                                      plan=insurance_plan,
                                                                      **insurance_policy_serializer.validated_data)
                    return insurance_policy
                else:
                    raise ValidationError(insurance_policy_serializer.errors)
        except Exception as e:
            raise ValidationError(f"Transaction failed: {str(e)}")
