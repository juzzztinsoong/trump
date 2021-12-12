# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-15 06:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trump2', '0004_auto_20170815_1429'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='dayeven',
        ),
        migrations.RemoveField(
            model_name='course',
            name='dayodd',
        ),
        migrations.AddField(
            model_name='course',
            name='day',
            field=models.CharField(choices=[('MO', 'Monday'), ('TU', 'Tuesday'), ('WE', 'Wednesday'), ('TH', 'Thursday'), ('FR', 'Friday'), ('SA', 'Saturday'), ('SU', 'Sunday')], default='MO', max_length=2, verbose_name='Day of Lesson'),
            preserve_default=False,
        ),
    ]
