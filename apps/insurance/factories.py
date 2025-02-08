from .services import PasargadInsuranceService, HekmatInsuranceService


class InsuranceFactory:
    @staticmethod
    def get_service(insurance_company):
        match insurance_company:
            case "Pasargad":
                return PasargadInsuranceService()
            case "Hekmat":
                return HekmatInsuranceService()
            case _:
                raise ValueError("Insurance company not supported")
