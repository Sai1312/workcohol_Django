from rest_framework import generics
from .models import CompanyItem
from .serializers import CompanySerializer

class CompanyList(generics.ListCreateAPIView):
    queryset = CompanyItem.objects.all() 
    serializer_class = CompanySerializer 