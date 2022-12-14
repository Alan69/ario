from .models import Request, RequestTypeTwo, RequestTypeThree
from rest_framework import serializers

class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = '__all__'

class RequestTypeTwoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestTypeTwo
        fields = '__all__'

class RequestTypeThreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestTypeThree
        fields = '__all__'