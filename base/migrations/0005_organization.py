# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-05 19:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_asset_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.Location')),
            ],
        ),
    ]
