from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from apps.insurances.models import InsurancePolicy, Person, InsuranceCompany, Policyholder, InsurancePlan


class InsurancePolicyCreateTestCase(APITestCase):
    """
    Test case for creating an insurance policy via API.
    """

    def setUp(self):
        """
        Set up required data before running each test.
        """
        self.url = reverse("custom-person-create")  # Ensure this matches your URL name

        self.valid_payload = {
            "person": {
                "first_name": "sample_first_name",
                "last_name": "sample_last_name",
                "email": "sample@example.com",
                "phone_number": "+989191200000",
                "national_id_number": "0011001111",
                "birth_date": "2000-01-01",
                "father_name": "some_name",
                "issue_place": "some_city"
            },
            "insurance_company": {
                "name": "Pasargad",
                "unique_id": "894651"
            },
            "policy_holder": {
                "name": "Parham",
                "unique_policy_holder_id": "5464"
            },
            "insurance_plan": {
                "name": "Gold",
                "unique_plan_id": "894654"
            },
            "unique_policy_number": "3247897898",
            "start_date": "2024-02-12",
            "end_date": "2025-02-12",
            "confirmation_date": "2024-02-12"
        }

    def test_create_insurance_policy_success(self):
        """
        Test that a valid insurance policy is created successfully.
        """
        response = self.client.post(self.url, self.valid_payload, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(InsurancePolicy.objects.count(), 1)
        self.assertEqual(Person.objects.count(), 1)
        self.assertEqual(InsuranceCompany.objects.count(), 1)
        self.assertEqual(Policyholder.objects.count(), 1)
        self.assertEqual(InsurancePlan.objects.count(), 1)

        insurance_policy = InsurancePolicy.objects.first()
        self.assertEqual(insurance_policy.unique_policy_number, "3247897898")
        self.assertEqual(insurance_policy.person.first_name, "sample_first_name")
        self.assertEqual(insurance_policy.insurance_company.name, "Pasargad")
