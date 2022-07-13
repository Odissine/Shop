import imp
from django.db import models
from datetime import datetime, timedelta
from django.template.defaultfilters import slugify
from .core import get_nom_element


# INVENTAIRES
class Inventaire(models.Model):
    objects = models.Manager()
    start_date = models.DateTimeField(auto_now=True)
    end_date = models.DateTimeField(default=datetime.now() + timedelta(days=360))
    actif = models.BooleanField(default=False)

    def __str__(self):
        if self.end_date is not None:
            return str(self.start_date.year) + " - " + str(self.end_date.year)
        else:
            return str(self.start_date.year) + " - Maintenant"


# ESPECES
class Espece(models.Model):
    nom = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, null=True)

    def __str__(self):
        return self.nom

    def save(self, *args, **kwargs):
        if not self.slug or self.slug != slugify(self.nom):
            self.slug = slugify(self.nom)
        super(Espece, self).save(*args, **kwargs)


    @classmethod
    def get_default_espece(cls) -> "Espece":
        espece, _ = cls.objects.get_or_create(nom="Défaut", slug="_defaut")
        return espece.pk


# VARIETES
class Variete(models.Model):
    objects = models.Manager()
    nom = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, null=True, db_index=True)

    def __str__(self):
        return self.nom

    def save(self, *args, **kwargs):
        if not self.slug or self.slug != slugify(self.nom):
            self.slug = slugify(self.nom)
        super(Variete, self).save(*args, **kwargs)

    @classmethod
    def get_default_variete(cls) -> "Variete":
        variete, _ = cls.objects.get_or_create(nom="Défaut", slug="_defaut")
        return variete.pk


# PORTEGREFFES
class PorteGreffe(models.Model):
    objects = models.Manager()
    nom = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, null=True, db_index=True)

    def __str__(self):
        return self.nom

    def save(self, *args, **kwargs):
        if not self.slug or self.slug != slugify(self.nom):
            self.slug = slugify(self.nom)
        super(PorteGreffe, self).save(*args, **kwargs)

    @classmethod
    def get_default_portegreffe(cls) -> "PorteGreffe":
        portegreffe, _ = cls.objects.get_or_create(nom="Défaut", slug="_defaut")
        return portegreffe.pk


# SPECIALITES
class Specialite(models.Model):
    objects = models.Manager()
    nom = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, null=True, db_index=True)

    def __str__(self):
        return self.nom

    def save(self, *args, **kwargs):
        if not self.slug or self.slug != slugify(self.nom):
            self.slug = slugify(self.nom)
        super(Specialite, self).save(*args, **kwargs)

    @classmethod
    def get_default_specialite(cls) -> "Specialite":
        specialite, _ = cls.objects.get_or_create(nom="Défaut", slug="_defaut")
        return specialite.pk


# PRODUITS
class Produit(models.Model):
    objects = models.Manager()
    nom = models.CharField(max_length=250, null=True)
    slug = models.SlugField(max_length=250, db_index=True, blank=True)
    description = models.TextField(blank=True, null=True)
    prix = models.DecimalField(max_digits=10, decimal_places=2, default=15.00)

    espece = models.ForeignKey(Espece, related_name='Produits', default=Espece.get_default_espece, on_delete=models.SET_DEFAULT)
    variete = models.ForeignKey(Variete, related_name='Produits', default=Variete.get_default_variete, on_delete=models.SET_DEFAULT)
    portegreffe = models.ForeignKey(PorteGreffe, related_name='Produits', default=PorteGreffe.get_default_portegreffe, on_delete=models.SET_DEFAULT)
    specialite = models.ForeignKey(Specialite, related_name='Produits', default=Specialite.get_default_specialite, on_delete=models.SET_DEFAULT)

    stock_reel = models.IntegerField(default=0)
    stock_encours = models.IntegerField(default=0)
    stock_futur = models.IntegerField(default=0)
    available = models.BooleanField(default=True)
    gaf = models.BooleanField(default=False)

    def __str__(self):
        return self.nom

    def save(self, *args, **kwargs):
        # if not self.nom:
        #     print(self.espece.nom)
        #     self.nom = get_nom_element('espece', self.espece.pk) + "_" + get_nom_element('variete', self.variete.pk) + "_" + get_nom_element('portegreffe', self.portegreffe.pk) + "_" + get_nom_element('specialite', self.specialite.pk)

        if not self.slug or self.slug != slugify(self.nom):
            self.slug = slugify(self.nom)
        
        if self.stock_encours < 0:
            self.stock_encours = 0

        if self.stock_futur < 0:
            self.stock_futur = 0

        if self.stock_reel < 0:
            self.stock_reel = 0

        super(Specialite, self).save(*args, **kwargs)

# GREFFONS
class Greffon(models.Model):
    objects = models.Manager()
    produit = models.ForeignKey(Produit, related_name='Greffons', on_delete=models.CASCADE)
    greffon = models.IntegerField(default=0, null=True)
    comm = models.IntegerField(null=True)
    objectif = models.IntegerField(default=0, null=True)
    realise = models.IntegerField(default=0, null=True)
    reussi = models.IntegerField(default=0, null=True)
    date = models.DateTimeField(auto_now=True, null=True)
    inventaire = models.ForeignKey(Inventaire, related_name='Greffons', on_delete=models.CASCADE, null=True)
