from curses.ascii import SP
from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import EspeceSerializer, ProduitSerializer, VarieteSerializer, PorteGreffeSerializer, SpecialiteSerializer
from product.models import Espece, Produit, Variete, PorteGreffe, Specialite

# ESPECES --------------------------------------------------------------------------------
# GET ALL ESPECE OR ADD ANOTHER ESPECE
@api_view(['GET', 'POST',])
def espece_list(request):
    # GET LIST OF ESPECES
    if request.method == 'GET':
        especes = Espece.objects.all()
        serializer = EspeceSerializer(especes, many=True, context={'request': request})
        return Response(serializer.data)

    # ADD NEW ESPECE
    elif request.method == 'POST':
        serializer = EspeceSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
        

# GET ONE ESPECE OR MODIFY ON ELEMENT FROM ESPECE 
@api_view(['GET', 'PATCH', ])
def espece_detail(request, id):
    espece = get_object_or_404(Espece, pk=id)

    if request.method == 'GET':
        serializer = EspeceSerializer(espece)
        return Response(serializer.data)
    elif request.method == "PATCH":
        serializer = EspeceSerializer(espece, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


# VARIETES --------------------------------------------------------------------------------
# GET ALL VARIETES OR ADD ANOTHER VARIETE
@api_view(['GET', 'POST',])
def variete_list(request):
    # GET LIST OF VARIETES
    if request.method == 'GET':
        varietes = Variete.objects.all()
        serializer = VarieteSerializer(varietes, many=True, context={'request': request})
        return Response(serializer.data)

    # ADD NEW VARIETE
    elif request.method == 'POST':
        serializer = VarieteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
        

# GET ONE VARIETE OR MODIFY ON ELEMENT FROM VARIETE 
@api_view(['GET', 'PATCH', ])
def variete_detail(request, id):
    variete = get_object_or_404(Variete, pk=id)

    if request.method == 'GET':
        serializer = VarieteSerializer(variete)
        return Response(serializer.data)
    elif request.method == "PATCH":
        serializer = VarieteSerializer(variete, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


# PORTE GREFFE --------------------------------------------------------------------------------
# GET ALL PORTE GREFFE OR ADD ANOTHER PORTE GREFFE
@api_view(['GET', 'POST',])
def portegreffe_list(request):
    # GET LIST OF PORTE GREFFE
    if request.method == 'GET':
        portegreffes = PorteGreffe.objects.all()
        serializer = PorteGreffeSerializer(portegreffes, many=True, context={'request': request})
        return Response(serializer.data)

    # ADD NEW PORTE GREFFE
    elif request.method == 'POST':
        serializer = PorteGreffeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
        

# GET ONE PORTE GREFFE OR MODIFY ON ELEMENT FROM PORTE GREFFE 
@api_view(['GET', 'PATCH', ])
def portegreffe_detail(request, id):
    portegreffe = get_object_or_404(PorteGreffe, pk=id)

    if request.method == 'GET':
        serializer = PorteGreffeSerializer(portegreffe)
        return Response(serializer.data)
    elif request.method == "PATCH":
        serializer = PorteGreffeSerializer(portegreffe, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


# SPECIALITE --------------------------------------------------------------------------------
# GET ALL SPECIALITE OR ADD ANOTHER SPECIALITE
@api_view(['GET', 'POST',])
def specialite_list(request):
    # GET LIST OF SPECIALITE
    if request.method == 'GET':
        specialites = Specialite.objects.all()
        serializer = SpecialiteSerializer(specialites, many=True, context={'request': request})
        return Response(serializer.data)

    # ADD NEW SPECIALITE
    elif request.method == 'POST':
        serializer = SpecialiteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
        

# GET ONE SPECIALITE OR MODIFY ON ELEMENT FROM SPECIALITE
@api_view(['GET', 'PATCH', ])
def specialite_detail(request, id):
    specialite = get_object_or_404(Specialite, pk=id)

    if request.method == 'GET':
        serializer = SpecialiteSerializer(specialite)
        return Response(serializer.data)
    elif request.method == "PATCH":
        serializer = SpecialiteSerializer(specialite, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


# PRODUITS --------------------------------------------------------------------------------
# GET ALL PRODUITS OR ADD ANOTHER PRODUIT
@api_view(['GET', 'POST',])
def produits_list(request):
    # GET LIST OF PRODUITS
    if request.method == 'GET':
        produits = Produit.objects.all()
        serializer = ProduitSerializer(produits, many=True, context={'request': request})
        return Response(serializer.data)

    # ADD NEW PRODUIT
    elif request.method == 'POST':
        serializer = ProduitSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
        

# GET ONE PRODUIT OR MODIFY ON ELEMENT FROM PRODUIT
@api_view(['GET', 'PATCH', ])
def produit_detail(request, id):
    produit = get_object_or_404(Produit, pk=id)

    if request.method == 'GET':
        serializer = ProduitSerializer(produit)
        return Response(serializer.data)
    elif request.method == "PATCH":
        serializer = ProduitSerializer(produit, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

'''
# Version avec CLASS
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
