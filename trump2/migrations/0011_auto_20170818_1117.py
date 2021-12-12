# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-18 03:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trump2', '0010_auto_20170817_1110'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='abbr',
            field=models.CharField(default='SCH', help_text='Max. 5 characters', max_length=5),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='school',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]