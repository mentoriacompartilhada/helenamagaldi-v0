from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import ClientSerializer
from .models import Client

def hello_world(request):
    return HttpResponse('Hello World')

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all().order_by("nickname")
    serializer_class = ClientSerializer