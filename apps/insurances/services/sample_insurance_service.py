from django.db import transaction

from .base_insurance_service import BaseInsuranceService
from ..models.person import Person
from ..models.insurance_company import InsuranceCompany
from ..models.insurance_plan import InsurancePlan
from ..models.insurance_policy import InsurancePolicy
from ..models.policy_holder import Policyholder


from ..serializers import PersonSerializer, InsuranceCompanySerializer, PolicyholderSerializer


class SampleInsuranceService(BaseInsuranceService):

    def _create_policy_holder(data: dict) -> Policyholder:
        return PolicyholderSerializer()

    def _create_insurance_company(data: dict) -> InsuranceCompany:
        return InsuranceCompanySerializer()

    def _create_person(self, person: dict) -> Person:
        # specific policy of registering person
        return PersonSerializer().save()

    @transaction.atomic
    def create_insurance_policy(self, data: dict) -> InsurancePolicy:
        person = self._create_person(data["person"])
        insurance_company = self._create_insurance_company(data["insurance_company"])
        policy_holder = self._create_policy_holder(data["policy_holder"])
        insurance_policy = self._insurance_policy(data["insurance_policy"])
