# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-31 19:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0007_auto_20160913_1024'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubPlace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=120)),
                ('poiid', models.CharField(db_index=True, max_length=120)),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='location.Place')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='sub_place',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='location.SubPlace'),
        ),
    ]
