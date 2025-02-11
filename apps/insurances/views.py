from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import InsuranceCompany
# from .factories import InsuranceFactory

from rest_framework.viewsets import ModelViewSet
from .models.person import Person
from .serializers import PersonSerializer, InsuranceFormSerializer
from drf_yasg.utils import swagger_auto_schema


# class InsuranceDataReceiver(APIView):

#     def post(self, request):
#         data = request.data
#         insurance_company = InsuranceCompany.objects.filter(unique_id=data["insurance_company_id"]).first()

#         if not insurance_company:
#             return Response({"error": "Invalid insurance company ID"}, status=status.HTTP_400_BAD_REQUEST)

#         service = InsuranceFactory.get_service(insurance_company)
#         try:
#             person = service.process_data(data)
#             return Response({"message": "Data processed successfully", "person_id": person.id}, status=status.HTTP_201_CREATED)
#         except Exception as e:
#             return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class InsuranceFormCreateView(APIView):
    
    @swagger_auto_schema(request_body=InsuranceFormSerializer)
    def post(self, request):
        serializer = InsuranceFormSerializer(data=request.data)
        if serializer.is_valid():
            person = serializer.save()
            return Response({"message": "Person created successfully", "person_id": person.id}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PersonModelViewSet(ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
