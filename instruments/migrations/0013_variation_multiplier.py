# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-09 21:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instruments', '0012_instrument_multiplier'),
    ]

    operations = [
        migrations.AddField(
            model_name='variation',
            name='multiplier',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]