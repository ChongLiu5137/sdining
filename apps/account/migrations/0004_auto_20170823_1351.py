# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-23 13:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20170821_1103'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='accesstoken',
            options={'ordering': ['-date_create']},
        ),
    ]