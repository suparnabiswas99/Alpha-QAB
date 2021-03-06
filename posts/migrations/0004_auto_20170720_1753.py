# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-20 17:53
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20170718_1957'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='brief',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(max_length=10000, null=True),
        ),
    ]
