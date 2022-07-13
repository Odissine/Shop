from django.shortcuts import render
from django.apps import apps
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from .serializers import *
from .models import *

from django.shortcuts import get_object_or_404, redirect
from .models import Espece
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView


class ElementList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'element_list.html'

    def get(self, request, element):
        Model = apps.get_model('product', str(element).capitalize())
        queryset = Model.objects.all()
        return Response({'elements': queryset})


class ElementDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'element_detail.html'

    def get(self, request, element, pk):
        Model = apps.get_model('product', str(element).capitalize())
        element = get_object_or_404(Model, pk=pk)
        serializer = EspeceSerializer(element)
        return Response({'serializer': serializer, 'element': element})

    def post(self, request, element, pk):
        Model = apps.get_model('product', str(element).capitalize())
        element = get_object_or_404(Model, pk=pk)
        serializer = EspeceSerializer(element, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'element': element})
        serializer.save()
        return redirect('element-list')


'''
# GET ALL ELEMENTS ---------------------------------------------------------------------------------------------------------
@api_view(['GET'])
def all_especes(request):
    especes = Espece.objects.all()
    serialization = EspeceSerializer(especes, many=True)
    return JsonResponse(serialization.data, safe=False)


@api_view(['GET'])
def all_varietes(request):
    varietes = Variete.objects.all()
    serialization = VarieteSerializer(varietes, many=True)
    return Response(serialization.data)


@api_view(['GET'])
def all_portegreffes(request):
    portegreffes = PorteGreffe.objects.all()
    serialization = PorteGreffeSerializer(portegreffes, many=True)
    return Response(serialization.data)


@api_view(['GET'])
def all_specialites(request):
    specialites = Specialite.objects.all()
    serialization = SpecialiteSerializer(specialites, many=True)
    return Response(serialization.data)


@api_view(['GET'])
def all_produits(request):
    produits = Produit.objects.all()
    serialization = ProduitSerializer(produits, many=True)
    return Response(serialization.data)


@api_view(['GET'])
def all_greffons(request):
    greffons = Greffon.objects.all()
    serialization = GreffonSerializer(greffons, many=True)
    return Response(serialization.data)


@api_view(['GET'])
def all_inventaires(request):
    inventaires = Inventaire.objects.all()
    serialization = InventaireSerializer(inventaires, many=True)
    return Response(serialization.data)


# GET ONE ELEMENT ---------------------------------------------------------------------------------------------------------
@api_view(['GET'])
def get_espece(request, id):
    espece = Espece.objects.get(pk=id)
    serializer = EspeceSerializer(espece)
    return Response(serializer.data)


@api_view(['GET'])
def get_variete(request, id):
    variete = Variete.objects.get(pk=id)
    serializer = VarieteSerializer(variete)
    return Response(serializer.data)


@api_view(['GET'])
def get_portegreffe(request, id):
    portegreffe = PorteGreffe.objects.get(pk=id)
    serializer = PorteGreffeSerializer(portegreffe)
    return Response(serializer.data)


@api_view(['GET'])
def get_specialite(request, id):
    specialite = Specialite.objects.get(pk=id)
    serializer = SpecialiteSerializer(specialite)
    return Response(serializer.data)


@api_view(['GET'])
def get_produit(request, id):
    produit = Produit.objects.get(pk=id)
    serializer = ProduitSerializer(produit)
    return Response(serializer.data)


@api_view(['GET'])
def get_greffon(request, id):
    greffon = Greffon.objects.get(pk=id)
    serializer = GreffonSerializer(greffon)
    return Response(serializer.data)


@api_view(['GET'])
def get_inventaire(request, id):
    inventaire = Inventaire.objects.get(pk=id)
    serializer = InventaireSerializer(inventaire)
    return Response(serializer.data)


# ADD ONE ELEMENT ---------------------------------------------------------------------------------------------------------
@api_view(['POST'])
def add_espece(request):
    serializer = EspeceSerializer(data=request.data, many=True)
    if serializer.is_valid():
        serializer.save()
    return JsonResponse(serializer.data, safe=False)
'''