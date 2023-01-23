from .models import International, Student, Courses
from rest_framework import serializers

class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = International
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = '__all__'