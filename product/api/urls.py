
from django.urls import path
from product.api.views import *


urlpatterns = [
    path('especes/', espece_list),
    path('espece/<id>/', espece_detail),

    path('varietes/', variete_list),
    path('variete/<id>/', variete_detail),

    path('portegreffes/', portegreffe_list),
    path('portegreffe/<id>/', portegreffe_detail),

    path('specialites/', specialite_list),
    path('specialite/<id>/', specialite_detail),

    path('produits/', produits_list),
    path('produit/<id>/', produit_detail),
]
