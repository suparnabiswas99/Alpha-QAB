# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-31 05:03
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_auto_20170725_0807'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-timestamp', '-updated']},
        ),
        migrations.AddField(
            model_name='profile',
            name='pic',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(max_length=1000000, null=True),
        ),
    ]
