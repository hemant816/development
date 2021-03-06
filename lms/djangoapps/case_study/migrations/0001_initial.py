# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-28 11:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='case_study_abstracts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=255)),
                ('description', models.TextField(blank=True)),
                ('uploaded_file', models.CharField(blank=True, db_index=True, max_length=500)),
                ('user_type', models.CharField(choices=[(b'dr', b'Doctor'), (b'prof', b'Professor'), (b'std', b'Student'), (b'team', b'Team')], db_index=True, default=b'dr', max_length=5)),
                ('case_study_type', models.CharField(choices=[(b'Observational (non-experimental) studies', ((b'chrt-stds', b'Cohort studies'), (b'case-cntrl', b'Case control studies'), (b'rdbs', b'Routine-data-based studies'), (b'drs', b'Dose-response studies'))), (b'Intervention (experimental) studies', ((b'cl', b'Clinical trials'), (b'fli', b'Field trials(individual level)'), (b'fla', b'Field trials(aggregated level)')))], db_index=True, max_length=10)),
                ('author_name', models.CharField(blank=True, max_length=500, null=True)),
                ('author_email', models.CharField(blank=True, max_length=500, null=True)),
                ('author_affiliation', models.CharField(blank=True, max_length=500, null=True)),
                ('tos', models.CharField(blank=True, max_length=5, null=True)),
                ('csa_updated', models.DateTimeField(auto_now=True)),
                ('csa_added', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='case_study_abstracts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
