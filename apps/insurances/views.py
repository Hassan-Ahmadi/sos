from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models.person import Person
from .factories import InsuranceCompanyFactory

from rest_framework.viewsets import ModelViewSet
from .models.person import Person
from .serializers import PersonSerializer, InsuranceFormSerializer
from drf_yasg.utils import swagger_auto_schema


class InsurancePolicyCreateView(APIView):
    
    @swagger_auto_schema(request_body=InsuranceFormSerializer)
    def post(self, request):
        data=request.data
        serializer = InsuranceFormSerializer(data=data)
        if serializer.is_valid():
            insurance_company_name = data["insurance_company"]["name"]
            try:
                service = InsuranceCompanyFactory.get_service(insurance_company_name)
                insurance_policy = service.create_insurance_policy(data=data)
                return Response({"message": "Insurance Policy created successfully"}, status=status.HTTP_201_CREATED)
            except ValueError:
                return Response({"message": "Insurance company not supported"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PersonModelViewSet(ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
