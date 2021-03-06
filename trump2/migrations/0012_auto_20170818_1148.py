# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-18 03:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trump2', '0011_auto_20170818_1117'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='course_id',
        ),
        migrations.RemoveField(
            model_name='instructor',
            name='instructor_id',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='date',
        ),
        migrations.RemoveField(
            model_name='school',
            name='school_id',
        ),
        migrations.AddField(
            model_name='course',
            name='id',
            field=models.AutoField(auto_created=True, default='2', primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='instructor',
            name='id',
            field=models.AutoField(auto_created=True, default='2', primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='school',
            name='id',
            field=models.AutoField(auto_created=True, default='2', primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='lesson',
            name='endTime',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='startTime',
            field=models.DateTimeField(),
        ),
    ]
