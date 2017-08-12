# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-11 11:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0015_user_usertype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='usertype',
            field=models.IntegerField(choices=[(0, '商家'), (1, '用户')], default=1, verbose_name='用户类型'),
        ),
    ]