# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-24 13:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storefrontend', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about',
            old_name='about',
            new_name='about_one',
        ),
        migrations.AddField(
            model_name='about',
            name='about_two',
            field=models.TextField(default=' Our dirt is quality dirt. We will ship you (or the person you designate) dirt in an envelope. This is your chance to have dirt shipped via the mail!'),
            preserve_default=False,
        ),
    ]
