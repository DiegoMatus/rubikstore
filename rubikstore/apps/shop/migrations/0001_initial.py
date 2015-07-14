# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Base',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, null=True, unique=True, max_length=40)),
                ('description', models.TextField(blank=True, null=True)),
                ('description_full', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='brand/%Y%m%d', blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, null=True, unique=True, max_length=40)),
                ('code', models.BigIntegerField(blank=True, null=True, max_length=10)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='category/%Y%m%d', blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True, default=datetime.datetime(2015, 7, 14, 1, 34, 43, 590733))),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ImageProduct',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('image', models.ImageField(upload_to='product/%Y%m%d')),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('volume', models.IntegerField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('price', models.DecimalField(max_digits=10, decimal_places=2)),
                ('slug', models.SlugField(blank=True, null=True, unique=True, max_length=40)),
                ('off', models.IntegerField(blank=True, choices=[(1, 10), (2, 20), (3, 30), (4, 40), (5, 50), (6, 60), (7, 70), (8, 80), (9, 90), (10, 100)], null=True, max_length=1)),
                ('description', models.TextField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('description_full', models.TextField(blank=True, null=True)),
                ('code', models.BigIntegerField(blank=True, null=True, max_length=10)),
                ('views', models.IntegerField(blank=True, null=True, max_length=10)),
                ('type', models.IntegerField(choices=[(1, 'Puzzle'), (2, 'Timers'), (3, 'Accessory')], default=1)),
                ('thumbnail', models.FileField(upload_to='thumbnails/%Y%m%d', blank=True, null=True)),
                ('featured', models.BooleanField(default=False)),
                ('base', models.ManyToManyField(blank=True, to='shop.Base', null=True)),
                ('brand', models.ForeignKey(to='shop.Brand', related_name='products')),
                ('category', models.ForeignKey(to='shop.Category', related_name='products_c')),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=300)),
                ('country', models.ForeignKey(to='shop.Country', related_name='states')),
            ],
        ),
        migrations.AddField(
            model_name='inventory',
            name='product',
            field=models.ForeignKey(to='shop.Product', related_name='existence'),
        ),
        migrations.AddField(
            model_name='imageproduct',
            name='product',
            field=models.ForeignKey(to='shop.Product', related_name='images'),
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(to='shop.State', related_name='cities'),
        ),
    ]
