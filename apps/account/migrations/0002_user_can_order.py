# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-20 20:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='can_order',
            field=models.BooleanField(default=True, verbose_name='是否能订餐'),
        ),
    ]
