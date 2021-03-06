# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-28 11:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='webform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseid', models.CharField(max_length=100, verbose_name=b'Courseid')),
                ('sheeturl', models.CharField(max_length=300, verbose_name=b'Url')),
                ('name', models.CharField(max_length=100, verbose_name=b'Name')),
                ('location', models.CharField(max_length=200, verbose_name=b'Location')),
                ('question', models.CharField(max_length=200, verbose_name=b'Question')),
                ('feedback_form_link', models.CharField(max_length=500, verbose_name=b'Feedback Form Link')),
            ],
            options={
                'verbose_name': 'Google Forms',
                'verbose_name_plural': 'Google Forms',
            },
        ),
    ]
