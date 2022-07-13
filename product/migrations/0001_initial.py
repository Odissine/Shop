# Generated by Django 4.0.6 on 2022-07-07 21:54

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Espece',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Inventaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(auto_now=True)),
                ('end_date', models.DateTimeField(default=datetime.datetime(2023, 7, 2, 21, 54, 33, 740693))),
                ('actif', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='PorteGreffe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=250)),
                ('slug', models.SlugField(blank=True, max_length=250)),
                ('description', models.TextField(blank=True, null=True)),
                ('prix', models.DecimalField(decimal_places=2, default=15.0, max_digits=10)),
                ('stock_reel', models.IntegerField(default=0)),
                ('stock_encours', models.IntegerField(default=0)),
                ('stock_future', models.IntegerField(default=0)),
                ('available', models.BooleanField(default=True)),
                ('gaf', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Specialite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Variete',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Greffons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('greffons', models.IntegerField(default=0, null=True)),
                ('comm', models.IntegerField(null=True)),
                ('objectif', models.IntegerField(default=0, null=True)),
                ('realise', models.IntegerField(default=0, null=True)),
                ('reussi', models.IntegerField(default=0, null=True)),
                ('date', models.DateTimeField(auto_now=True, null=True)),
                ('inventaire', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Greffons', to='product.inventaire')),
                ('produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Greffons', to='product.produit')),
            ],
        ),
    ]
