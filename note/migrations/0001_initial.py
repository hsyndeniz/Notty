# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-12 22:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Başlık')),
                ('content', models.TextField(verbose_name='İçerik')),
                ('created_at', models.DateField(verbose_name='Yayın Tarihi')),
                ('doc', models.FileField(upload_to='', verbose_name='Döküman')),
            ],
        ),
    ]