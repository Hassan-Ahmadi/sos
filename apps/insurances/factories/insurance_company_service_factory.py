from ..services.pasargad_insurance_service import PasargadInsuranceService
from ..services.hekmat_insurance_service import HekmatInsuranceService


class InsuranceCompanyServiceFactory:
    """
    Factory class to get the appropriate insurance service based on the insurance company name.

    Methods:
        get_service(insurance_company: str) -> object:
            Static method that returns an instance of the insurance service corresponding to the given insurance company name.
            Raises a ValueError if the insurance company is not supported.

            Parameters:
                insurance_company (str): The name of the insurance company.

            Returns:
                object: An instance of the corresponding insurance service.
    """

    _handlers = {
        "pasargad": PasargadInsuranceService,
        "hekmat": HekmatInsuranceService,
    }
    
    @classmethod
    def get(cls, insurance_company: str):
        if insurance_company.lower() in cls._handlers:
            return cls._handlers.get(insurance_company.lower())
        else:
            raise ValueError("Insurance company not supported")
