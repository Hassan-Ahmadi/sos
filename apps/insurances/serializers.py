from rest_framework import serializers
from .models.person import Person
from .models.insurance_company import InsuranceCompany
from .models.policy_holder import Policyholder
from .models.insurance_policy import InsurancePolicy
from .models.insurance_plan import InsurancePlan

# from .factories.insurance_company_service_factory import InsuranceCompanyServiceFactory
# from .factories.insurance_company_adapters_factory import InsuranceCompanyAdaptorsFactory

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
    policyholder = PolicyholderSerializer()
    insurance_plan = InsurancePlanSerializer()
    class Meta:
        model = InsurancePolicy
        fields = "__all__"
        # fields = ("unique_policy_number", "start_date", "end_date", "confirmation_date")
    
    def validate(self, data):
        """
        Check that the start date is before the end date.
        """
        if data['start_date'] >= data['end_date']:
            raise serializers.ValidationError("End date must be after start date")
        return data
    
    # def create(self, validated_data):
    #     request = self.context.get("request")
    #     raw_data = request.data

    #     try:
    #         insurance_company_name = raw_data.get("insurance_company", {}).get("name")
    #         adapter = InsuranceCompanyAdaptorsFactory.get(insurance_company_name)
    #     except ValueError:
    #         raise serializers.ValidationError("Insurance company not supported")

    #     serializer_class = adapter.get_serializer_class()
    #     serializer = serializer_class(data=raw_data)
    #     if serializer.is_valid():
    #         validated_data = serializer.validated_data
    #     else:
    #         raise serializers.ValidationError(serializer.errors)

    #     person_data = validated_data.pop('person')
    #     insurance_company_data = validated_data.pop('insurance_company')
    #     policyholder_data = validated_data.pop('policyholder')
    #     insurance_policy_data = validated_data.pop('insurance_policy')
    #     insurance_plan_data = validated_data.pop('insurance_plan')

    #     start_date = insurance_policy_data['start_date']
    #     end_date = insurance_policy_data['end_date']

    #     existing_person = Person.objects.filter(**person_data).first()
    #     existing_insurance_company = InsuranceCompany.objects.filter(**insurance_company_data).first()
    #     existing_policyholder = Policyholder.objects.filter(**policyholder_data).first()
    #     existing_insurance_plan = InsurancePlan.objects.filter(**insurance_plan_data).first()
    #     existing_insurance_policy = InsurancePolicy.objects.filter(
    #         person=existing_person,
    #         insurance_company=existing_insurance_company,
    #         policyholder=existing_policyholder,
    #         insurance_plan=existing_insurance_plan,
    #         start_date=start_date,
    #         end_date=end_date
    #     ).first()

    #     if existing_insurance_policy:
    #         raise serializers.ValidationError("An insurance policy with the same details already exists.")

    #     person = existing_person if existing_person else Person.objects.create(**person_data)
    #     insurance_company = existing_insurance_company if existing_insurance_company else InsuranceCompany.objects.create(**insurance_company_data)
    #     policyholder = existing_policyholder if existing_policyholder else Policyholder.objects.create(**policyholder_data)
    #     insurance_plan = existing_insurance_plan if existing_insurance_plan else InsurancePlan.objects.create(**insurance_plan_data)
    #     insurance_policy = InsurancePolicy.objects.create(
    #         person=person,
    #         insurance_company=insurance_company,
    #         policyholder=policyholder,
    #         insurance_plan=insurance_plan,
    #         **insurance_policy_data
    #     )

    #     return {
    #         'person': person,
    #         'insurance_company': insurance_company,
    #         'policyholder': policyholder,
    #         'insurance_policy': insurance_policy,
    #         'insurance_plan': insurance_plan
    #     }


# class InsuranceFormSerializer(serializers.Serializer):
#     person = PersonSerializer()
#     insurance_company = InsuranceCompanySerializer()
#     policyholder = PolicyholderSerializer()
#     insurance_policy = InsurancePolicySerializer()
#     insurance_plan = InsurancePlanSerializer()
    
#     def create(self, validated_data):
#         person_data = validated_data.pop('person')
#         insurance_company_data = validated_data.pop('insurance_company')
#         policyholder_data = validated_data.pop('policyholder')
#         insurance_policy_data = validated_data.pop('insurance_policy')
#         insurance_plan_data = validated_data.pop('insurance_plan')
        
#         # Check if all entities with the same start_date and end_date exist
#         start_date = insurance_policy_data['start_date']
#         end_date = insurance_policy_data['end_date']
        
        
#         existing_person = Person.objects.filter(**person_data).first()
#         existing_insurance_company = InsuranceCompany.objects.filter(**insurance_company_data).first()
#         existing_policyholder = Policyholder.objects.filter(**policyholder_data).first()
#         existing_insurance_plan = InsurancePlan.objects.filter(**insurance_plan_data).first()
#         existing_insurance_policy = InsurancePolicy.objects.filter(
#             person=existing_person,
#             insurance_company=existing_insurance_company,
#             policyholder=existing_policyholder,
#             insurance_plan=existing_insurance_plan,
#             start_date=start_date,
#             end_date=end_date
#         ).first()

#         if existing_insurance_policy:
#             raise serializers.ValidationError("An insurance policy with the same details already exists.")

#         # If entities exist individually, return the existing objects
#         person = existing_person if existing_person else Person.objects.create(**person_data)
#         insurance_company = existing_insurance_company if existing_insurance_company else InsuranceCompany.objects.create(**insurance_company_data)
#         policyholder = existing_policyholder if existing_policyholder else Policyholder.objects.create(**policyholder_data)
#         insurance_plan = existing_insurance_plan if existing_insurance_plan else InsurancePlan.objects.create(**insurance_plan_data)
#         insurance_policy = InsurancePolicy.objects.create(
#             person=person,
#             insurance_company=insurance_company,
#             policyholder=policyholder,
#             insurance_plan=insurance_plan,
#             **insurance_policy_data
#         )

#         return {
#             'person': person,
#             'insurance_company': insurance_company,
#             'policyholder': policyholder,
#             'insurance_policy': insurance_policy,
#             'insurance_plan': insurance_plan
#         }
