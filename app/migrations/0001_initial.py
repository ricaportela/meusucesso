# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-05 20:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Participantes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('empresa', models.CharField(max_length=100)),
                ('profissao', models.CharField(max_length=100)),
                ('area_atuacao', models.CharField(max_length=100)),
                ('foto', models.ImageField(upload_to='upload/images/')),
            ],
        ),
    ]