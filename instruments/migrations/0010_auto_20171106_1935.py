# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-06 19:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instruments', '0009_auto_20171106_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instrument',
            name='title',
            field=models.CharField(max_length=60),
        ),
    ]
