from .services.pasargad_insurance_service import PasargadInsuranceService, HekmatInsuranceService

from .exceptions import UnsupportedInsuranceCompanyError


class InsuranceFactory:
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

    @staticmethod
    def get_service(insurance_company):
        match insurance_company:
            case "Pasargad":
                return PasargadInsuranceService()
            case "Hekmat":
                return HekmatInsuranceService()
            case _:
                raise ValueError("Insurance company not supported")
