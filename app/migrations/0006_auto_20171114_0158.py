# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-14 01:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_update'),
    ]

    operations = [
        migrations.AddField(
            model_name='app',
            name='storage_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='update',
            name='storage_name',
            field=models.CharField(default='', max_length=100),
        ),
    ]