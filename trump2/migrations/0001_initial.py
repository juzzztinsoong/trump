# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-15 06:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_id', models.AutoField(primary_key=True, serialize=False)),
                ('level', models.CharField(choices=[('P', 'Primary'), ('S', 'Secondary'), ('T', 'JC/Poly/ITE'), ('C', 'Corporate'), ('O', 'Others')], max_length=1)),
                ('group', models.CharField(blank=True, max_length=20, verbose_name='Class')),
                ('name', models.CharField(choices=[('CEP Year 4', 'CEP Year 4'), ('Android Advanced', 'Android Advanced'), ('Strawbees Design Thinking', 'Strawbees Design Thinking')], max_length=100, verbose_name='Course Name')),
                ('startDate', models.DateField(help_text='Enter in dd/mm/yyyy format', verbose_name='Start Date')),
                ('endDate', models.DateField(help_text='Enter in dd/mm/yyyy format', verbose_name='End Date')),
                ('startTime', models.TimeField(help_text='Enter in hh:mm format', verbose_name='Start Time')),
                ('endTime', models.TimeField(help_text='Enter in hh:mm format', verbose_name='End Time')),
                ('dayeven', models.CharField(blank=True, choices=[('MO', 'Monday'), ('TU', 'Tuesday'), ('WE', 'Wednesday'), ('TH', 'Thursday'), ('FR', 'Friday'), ('SA', 'Saturday'), ('SU', 'Sunday')], max_length=2, verbose_name='Day of Lesson on Even Weeks')),
                ('dayodd', models.CharField(blank=True, choices=[('MO', 'Monday'), ('TU', 'Tuesday'), ('WE', 'Wednesday'), ('TH', 'Thursday'), ('FR', 'Friday'), ('SA', 'Saturday'), ('SU', 'Sunday')], max_length=2, verbose_name='Day of Lesson on Odd Weeks')),
                ('interval', models.IntegerField(default=1, verbose_name='Number of Weeks Between Each Lesson')),
                ('contact', models.CharField(max_length=200, verbose_name='Name of Teacher-in-charge')),
                ('email', models.EmailField(max_length=254, verbose_name='Email Address of Teacher-in-charge')),
                ('number', models.CharField(blank=True, max_length=20, verbose_name='Contact Number of Teacher-in-charge')),
                ('updated', models.BooleanField(default=False, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('instructor_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('toe', models.CharField(choices=[('FT', 'Full-time'), ('FL', 'Freelance'), ('IN', 'Intern'), ('PT', 'Part-time')], max_length=2, verbose_name='Terms of Employment')),
                ('email', models.EmailField(max_length=254, verbose_name='Email Address')),
                ('hp', models.CharField(blank=True, max_length=20, verbose_name='Contact Number')),
                ('moe_expiry', models.DateField(null=True, verbose_name='MOE Expiry Date')),
                ('active', models.BooleanField(default=False)),
                ('location', models.CharField(choices=[('N', 'North'), ('E', 'East'), ('S', 'South'), ('W', 'West'), ('C', 'Central')], max_length=1)),
                ('remarks', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson_id', models.IntegerField()),
                ('calendar_event_id', models.URLField()),
                ('date', models.DateField()),
                ('startTime', models.TimeField()),
                ('endTime', models.TimeField()),
                ('comments', models.TextField(blank=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trump2.Course')),
                ('instructors', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trump2.Instructor')),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('school_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(choices=[('RI', 'Raffles Institution'), ('HCI', 'Hwa Chong Institution'), ('CWSS', 'Commonwealth Secondary School')], max_length=4)),
                ('location', models.CharField(choices=[('N', 'North'), ('E', 'East'), ('S', 'South'), ('W', 'West'), ('C', 'Central')], max_length=1)),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trump2.Instructor'),
        ),
        migrations.AddField(
            model_name='course',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trump2.School'),
        ),
    ]
