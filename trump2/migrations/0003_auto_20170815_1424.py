# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-15 06:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trump2', '0002_auto_20170815_1423'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='pdated',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AddField(
            model_name='lesson',
            name='lesson_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
