from rest_framework import serializers
from .models.person import Person
from .models.insurance_company import InsuranceCompany
from .models.policy_holder import Policyholder
from .models.insurance_policy import InsurancePolicy
from .models.insurance_plan import InsurancePlan


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = "__all__"
        extra_kwargs = {
            "email": {"validators": []},
            "phone_number": {"validators": []},
        }


class InsuranceCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = InsuranceCompany
        fields = "__all__"


class PolicyholderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Policyholder
        fields = "__all__"


class InsurancePolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = InsurancePolicy
        # fields = "__all__"
        fields = ("unique_policy_number", "start_date", "end_date", "confirmation_date")


class InsurancePlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = InsurancePlan
        fields = "__all__"

class InsuranceFormSerializer(serializers.Serializer):
    person = PersonSerializer()
    insurance_company = InsuranceCompanySerializer()
    policyholder = PolicyholderSerializer()
    insurance_policy = InsurancePolicySerializer()
    insurance_plan = InsurancePlanSerializer()
