# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-15 23:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('asset_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='base.Asset')),
                ('serial_number', models.CharField(max_length=20)),
            ],
            bases=('base.asset',),
        ),
    ]
