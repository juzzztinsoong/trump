# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-15 07:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trump2', '0006_auto_20170815_1516'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='updated',
            field=models.BooleanField(default=False, editable=False),
        ),
    ]