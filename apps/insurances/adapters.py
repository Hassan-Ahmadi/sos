from rest_framework import serializers

from .serializers import InsurancePolicySerializer


class BaseInsurancePolicyAdapter:
    def get_serializer_class(self) -> serializers.Serializer:
        return InsurancePolicySerializer


class PasargadInsuranceCompanyAdapter(BaseInsurancePolicyAdapter):
    def get_serializer_class(self) -> serializers.Serializer:
        class CustomSerializer(InsurancePolicySerializer):
            # Some custom serialization here!
            # full_name = serializers.CharField(source="first_name")
            pass

        return CustomSerializer


class HekamtInsuranceCompanyAdapter(BaseInsurancePolicyAdapter):
    def get_serializer_class(self) -> serializers.Serializer:
        class CustomSerializer(InsurancePolicySerializer):
            # Some custom serialization here!
            
            # first_name = serializers.CharField(source="first_name")
            # last_name = serializers.CharField(source="last_name")
            pass

        return CustomSerializer
