# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-06-05 10:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course_extrainfo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course_extrainfo',
            name='specialization',
            field=models.ForeignKey(default=16, null=True, on_delete=django.db.models.deletion.CASCADE, to='specialization.specializations'),
        ),
    ]
