# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-25 08:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='location',
            new_name='bio',
        ),
    ]
