# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-13 09:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0004_auto_20160913_0827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='weibo_img',
            field=models.URLField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='weibo_thumb_img',
            field=models.URLField(blank=True, max_length=150, null=True),
        ),
    ]
