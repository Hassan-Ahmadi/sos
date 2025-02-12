from rest_framework import serializers
from django.db import transaction

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


class InsurancePlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = InsurancePlan
        fields = "__all__"


class InsurancePolicySerializer(serializers.ModelSerializer):
    person = PersonSerializer()
    insurance_company = InsuranceCompanySerializer()
    policy_holder = PolicyholderSerializer()
    insurance_plan = InsurancePlanSerializer()
    class Meta:
        model = InsurancePolicy
        fields = "__all__"

    def validate(self, data):
        """
        Check that the start date is before the end date.
        """
        if data['start_date'] >= data['end_date']:
            raise serializers.ValidationError("End date must be after start date")
        return data

    def create(self, validated_data):
        """
        Handle nested object creation while avoiding duplicates.
        """
        # Extract nested data
        person_data = validated_data.pop("person")
        insurance_company_data = validated_data.pop("insurance_company")
        policy_holder_data = validated_data.pop("policy_holder")
        insurance_plan_data = validated_data.pop("insurance_plan", None)

        with transaction.atomic():  # Ensure everything is saved together
            # Fetch or create related objects
            person, _ = Person.objects.get_or_create(
                national_id_number=person_data["national_id_number"], defaults=person_data
            )
            insurance_company, _ = InsuranceCompany.objects.get_or_create(
                unique_id=insurance_company_data["unique_id"], defaults=insurance_company_data
            )
            policy_holder, _ = Policyholder.objects.get_or_create(
                unique_policy_holder_id=policy_holder_data["unique_policy_holder_id"], defaults=policy_holder_data
            )

            insurance_plan = None
            if insurance_plan_data:
                insurance_plan, _ = InsurancePlan.objects.get_or_create(
                    unique_plan_id=insurance_plan_data["unique_plan_id"], defaults=insurance_plan_data
                )

            # Create the insurance policy
            insurance_policy = InsurancePolicy.objects.create(
                person=person,
                insurance_company=insurance_company,
                policy_holder=policy_holder,
                insurance_plan=insurance_plan,
                **validated_data
            )

        return insurance_policy
