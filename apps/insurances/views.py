from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from apps.insurances.factories.insurance_company_adapters_factory import InsuranceCompanyAdaptorsFactory

from .serializers import InsurancePolicySerializer


class InsurancePolicyCreateView(APIView):
    
    @swagger_auto_schema(request_body=InsurancePolicySerializer)
    def post(self, request):
        """
        Handle POST request to create an insurance policy.
        """
        data = request.data
        insurance_company_name = data.get("insurance_company", {}).get("name")

        if not insurance_company_name:
            return Response({"message": "Insurance company name is required"}, status=status.HTTP_400_BAD_REQUEST)

        # Get the correct adapter and its serializer
        adapter = InsuranceCompanyAdaptorsFactory.get(insurance_company_name)
        serializer_class = adapter.get_serializer_class()
        serializer = serializer_class(data=data, context={'request': request})
        
        if serializer.is_valid():
            insurance_policy = serializer.save()
            return Response(
                {
                    "message": "Insurance policy created successfully",
                    "data": InsurancePolicySerializer(insurance_policy).data
                },
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
