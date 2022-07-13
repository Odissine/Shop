from rest_framework import serializers
from product.models import *


class InventaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventaire
        fields = ['start_date', 'end_date', 'actif']


class EspeceSerializer(serializers.ModelSerializer):
    nom = serializers.CharField()
    slug = serializers.SlugField()

    class Meta:
        model = Espece
        fields = ['id', 'nom', 'slug']


class VarieteSerializer(serializers.ModelSerializer):
    nom = serializers.CharField()
    slug = serializers.SlugField()

    class Meta:
        model = Variete
        fields = ['id', 'nom', 'slug']


class PorteGreffeSerializer(serializers.ModelSerializer):
    nom = serializers.CharField()
    slug = serializers.SlugField()

    class Meta:
        model = PorteGreffe
        fields = ['id', 'nom', 'slug']


class SpecialiteSerializer(serializers.ModelSerializer):
    nom = serializers.CharField()
    slug = serializers.SlugField()

    class Meta:
        model = Specialite
        fields = ['id', 'nom', 'slug']


class ProduitSerializer(serializers.ModelSerializer):
    
    espece = EspeceSerializer()
    variete = VarieteSerializer()
    portegreffe = PorteGreffeSerializer()
    specialite = SpecialiteSerializer()

    class Meta:
        model = Produit
        fields = ['nom', 'slug', 'description', 'prix', 'espece', 'variete', 'portegreffe', 'specialite', 'stock_reel', 'stock_encours', 'stock_futur', 'available', 'gaf']

    

class GreffonSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Greffon
        fields = ['produit', 'greffon', 'comm', 'objectif', 'realise', 'reussi', 'date', 'inventaire']
