from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import InsuranceCompany
from .factories import InsuranceFactory


class InsuranceDataReceiver(APIView):

    def post(self, request):
        data = request.data
        insurance_company = InsuranceCompany.objects.filter(unique_id=data["insurance_company_id"]).first()

        if not insurance_company:
            return Response({"error": "Invalid insurance company ID"}, status=status.HTTP_400_BAD_REQUEST)

        service = InsuranceFactory.get_service(insurance_company)
        try:
            person = service.process_data(data)
            return Response({"message": "Data processed successfully", "person_id": person.id}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
