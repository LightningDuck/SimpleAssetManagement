# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-03 21:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_auto_20170518_0132'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='description',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.AssetDescription'),
        ),
    ]
