# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-02-27 10:18
from __future__ import unicode_literals

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20180226_1323'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='author',
            field=models.CharField(default=django.contrib.auth.models.User, max_length=50),
        ),
        migrations.AlterField(
            model_name='notes',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='notes',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
