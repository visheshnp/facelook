# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-18 15:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('likes', '0004_auto_20160618_2057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likes',
            name='card',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='cards.Cards'),
        ),
    ]
