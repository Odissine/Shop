from rest_framework import serializers
from .models import *


class InventaireSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Inventaire
        fields = ['start_date', 'end_date', 'actif']


class VarieteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variete
        fields = ['nom', 'slug']


class EspeceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Espece
        fields = ['nom', 'slug']


class PorteGreffeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PorteGreffe
        fields = ['nom', 'slug']


class SpecialiteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Specialite
        fields = ['nom', 'slug']


class ProduitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Produit
        fields = ['nom', 'slug', 'description', 'prix', 'espece', 'variete', 'portegreffe', 'specialite', 'stock_reel', 'stock_encours', 'stock_futur', 'available', 'gaf']


class GreffonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Greffon
        fields = ['produit', 'greffon', 'comm', 'objectif', 'realise', 'reussi', 'date', 'inventaire']
