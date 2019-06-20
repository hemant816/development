# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-28 11:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cat_sub_category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic_name', models.CharField(max_length=50)),
                ('topic_short_name', models.CharField(max_length=50, null=True)),
                ('topic_image', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='specializations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name=b'Specialization')),
            ],
        ),
        migrations.CreateModel(
            name='sub_categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_topic_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='categories',
            name='sub_category',
            field=models.ManyToManyField(db_index=True, related_name='sub_category', to='specialization.sub_categories'),
        ),
        migrations.AddField(
            model_name='categories',
            name='topic_specialization',
            field=models.ManyToManyField(db_index=True, related_name='cat_specialization', to='specialization.specializations'),
        ),
        migrations.AddField(
            model_name='cat_sub_category',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='specialization.categories'),
        ),
    ]
