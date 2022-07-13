"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from product.views_api import *


urlpatterns = [
    # PATH FOR ALL DATA [ GET ] ------------------------------------------------------
    path('especes/', all_especes),
    path('varietes', all_varietes),
    path('portegreffes', all_portegreffes),
    path('specialites', all_specialites),
    path('produits', all_produits),
    path('greffons', all_greffons),
    path('inventaires', all_inventaires),

    # PATH FOR ONE DATA [ GET ] ------------------------------------------------------
    path('espece/<int:id>', get_espece),
    path('variete/<int:id>', get_variete),
    path('portegreffe/<int:id>', get_portegreffe),
    path('specialite/<int:id>', get_specialite),
    path('produit/<int:id>', get_produit),
    path('greffon/<int:id>', get_greffon),
    path('inventaire/<int:id>', get_inventaire),

    # PATH TO ADD DATA [ POST ] -------------------------------------------------------
    path('add/espece/', add_espece),
]
