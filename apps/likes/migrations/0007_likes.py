# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-18 15:43
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cards', '0010_remove_cards_likes'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('likes', '0006_auto_20160618_2109'),
    ]

    operations = [
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.IntegerField(default=0)),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('card', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='cards.Cards')),
                ('user', models.ManyToManyField(default='', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]