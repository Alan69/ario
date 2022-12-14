from .models import Request, RequestTypeTwo
from rest_framework import serializers

class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = '__all__'

class RequestTypeTwoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestTypeTwo
        fields = '__all__'