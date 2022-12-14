from .models import Request, RequestTypeTwo
from rest_framework.parsers import JSONParser
from .serializer import RequestSerializer, RequestTypeTwoSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

class RequestList(generics.ListCreateAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer

@api_view(['GET', 'PUT', 'DELETE'])
def request_detail(request, pk, format=None):
    try:
        request_obj = Request.objects.get(pk=pk)
    except Request.DoesNotExist:
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


class RequestTypeTwoList(generics.ListCreateAPIView):
    queryset = RequestTypeTwo.objects.all()
    serializer_class = RequestTypeTwoSerializer

@api_view(['GET', 'PUT', 'DELETE'])
def requestTypeTwo_detail(request, pk, format=None):
    try:
        request_obj = RequestTypeTwo.objects.get(pk=pk)
    except RequestTypeTwo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RequestTypeTwoSerializer(request_obj)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = RequestTypeTwoSerializer(request_obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        request_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)