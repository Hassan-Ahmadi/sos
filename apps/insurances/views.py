from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from drf_yasg.utils import swagger_auto_schema

from apps.insurances.factories.insurance_company_adapters_factory import InsuranceCompanyAdaptorsFactory
from .models.person import Person
from .serializers import PersonSerializer, InsurancePolicySerializer


class InsurancePolicyCreateView(APIView):
    
    @swagger_auto_schema(request_body=InsurancePolicySerializer)
    def post(self, request):
        """
        Handle POST request to create an insurance policy.
        """
        data = request.data
        insurance_company_name = data.get("insurance_company", {}).get("name")
        try:
            adapter = InsuranceCompanyAdaptorsFactory.get(insurance_company_name)
            serializer_class = adapter.get_serializer_class()
        except ValueError:
            return Response(
                {"message": "Insurance company not supported"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = serializer_class(data=data, context={'request': request})
        if serializer.is_valid():
            data = serializer.save()
            return Response(
                {
                    "message": "Data processed successfully",
                    "data": data
                },
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class PersonModelViewSet(ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
