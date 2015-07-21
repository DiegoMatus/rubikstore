# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20150714_0137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='volume',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='base',
            field=models.ManyToManyField(blank=True, to='shop.Base'),
        ),
        migrations.AlterField(
            model_name='product',
            name='code',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='off',
            field=models.IntegerField(blank=True, null=True, choices=[(1, 10), (2, 20), (3, 30), (4, 40), (5, 50), (6, 60), (7, 70), (8, 80), (9, 90), (10, 100)]),
        ),
        migrations.AlterField(
            model_name='product',
            name='views',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
