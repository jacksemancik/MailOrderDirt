# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-25 06:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('storefrontend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='slug',
            field=models.CharField(default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
    ]