# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-24 06:13
from __future__ import unicode_literals

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trump2', '0013_auto_20170818_1203'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='duration',
            field=models.DurationField(default=datetime.timedelta(0)),
        ),
        migrations.AlterField(
            model_name='course',
            name='endDate',
            field=models.DateField(verbose_name='Date of Last Lesson'),
        ),
        migrations.AlterField(
            model_name='course',
            name='interval',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1, message='Interval must be positive!')], verbose_name='Number of Weeks Between Each Lesson'),
        ),
        migrations.AlterField(
            model_name='course',
            name='startDate',
            field=models.DateField(verbose_name='Date of First Lesson'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='startTime',
            field=models.DateTimeField(verbose_name='Time of lesson'),
        ),
    ]