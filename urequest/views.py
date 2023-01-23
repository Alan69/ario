from django.shortcuts import render
from .models import International, Student, Courses
from rest_framework.parsers import JSONParser
from .serializer import RequestSerializer, StudentSerializer, CoursesSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
# Create your views here.
class RequestList(generics.ListCreateAPIView):
    queryset = International.objects.all()
    serializer_class = RequestSerializer

@api_view(['GET', 'PUT', 'DELETE'])
def request_detail(request, pk, format=None):
    try:
        request_obj = International.objects.get(pk=pk)
    except International.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RequestSerializer(request_obj)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = RequestSerializer(request_obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        request_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

@api_view(['GET', 'PUT', 'DELETE'])
def student_detail(request, pk, format=None):
    try:
        request_obj = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StudentSerializer(request_obj)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = StudentSerializer(request_obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        request_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CoursesList(generics.ListCreateAPIView):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer

@api_view(['GET', 'PUT', 'DELETE'])
def courses_detail(request, pk, format=None):
    try:
        request_obj = Courses.objects.get(pk=pk)
    except Courses.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CoursesSerializer(request_obj)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CoursesSerializer(request_obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        request_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)