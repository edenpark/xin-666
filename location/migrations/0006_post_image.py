# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-13 09:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0005_auto_20160913_0929'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=b'images'),
        ),
    ]