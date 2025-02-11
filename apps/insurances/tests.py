from rest_framework.test import APITestCase
from .models import InsuranceCompany


class InsuranceAPITestCase(APITestCase):

    def setUp(self):
        self.insurance_company = InsuranceCompany.objects.create(name="Pasargad", unique_id="PAS123")

    def test_valid_data_submission(self):
        data = {
            "insurance_company_id": "PAS123",
            "national_code": "1234567890",
            "first_name": "Ali",
            "last_name": "Ahmadi",
            "phone_number": "09121234567",
            "birth_date": "1990-01-01"
        }
        response = self.client.post("/api/insurance/", data, format="json")
        self.assertEqual(response.status_code, 201)
