from apps.insurances.serializers import serializers
from apps.insurances.adapters import (BaseInsurancePolicyAdapter,
                                      HekamtInsuranceCompanyAdapter,
                                      PasargadInsuranceCompanyAdapter)


class InsuranceCompanyAdaptorsFactory:

    _adapters = {
        "pasargad": PasargadInsuranceCompanyAdapter,
        "hekmat": HekamtInsuranceCompanyAdapter,
        # Add more companies here
    }

    @classmethod
    def get(cls, insurance_company: str) -> serializers.Serializer:
        adapter_class = cls._adapters.get(insurance_company.lower(), BaseInsurancePolicyAdapter)
        return adapter_class()
