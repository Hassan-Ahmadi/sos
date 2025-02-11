from .base_insurance_service import BaseInsuranceService
from ..models.person import Person
from ..models.insurance_company import InsuranceCompany
from ..models.insurance_plan import InsurancePlan
from ..models.insurance_policy import InsurancePolicy


class PasargadInsuranceService(BaseInsuranceService):

    def process_data(self, data):
        person, _ = Person.objects.get_or_create(
            national_code=data["national_code"],
            defaults={
                "first_name": data["first_name"],
                "last_name": data["last_name"],
                "email": data.get("email"),
                "phone_number": data["phone_number"],
                "birth_date": data["birth_date"],
            }
        )
        return person
