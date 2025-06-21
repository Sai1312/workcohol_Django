from rest_framework import serializers
from .models import CompanyItem

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model=CompanyItem
        fields='__all__'