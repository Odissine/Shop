from django.shortcuts import render, redirect, HttpResponse
from django.apps import apps
from django.contrib import messages
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import *

def index(request):
    context = {}
    return render(request, 'product/index.html', context)


class EspeceViewSet(viewsets.ModelViewSet):
    queryset = Espece.objects.all().order_by('slug')
    serializer_class = EspeceSerializer
    permission_classes = [permissions.IsAuthenticated]


class VarieteViewSet(viewsets.ModelViewSet):
    queryset = Variete.objects.all().order_by('slug')
    serializer_class = VarieteSerializer
    permission_classes = [permissions.IsAuthenticated]
