# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-17 03:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trump2', '0009_auto_20170815_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='calendar_event_id',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='instructors',
            field=models.ManyToManyField(blank=True, to='trump2.Instructor'),
        ),
    ]