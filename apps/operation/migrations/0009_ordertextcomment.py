# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-22 11:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0008_remove_order_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderTextComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(blank=True, max_length=150, verbose_name='评价')),
                ('date_comment', models.DateTimeField(auto_now_add=True, verbose_name='评论时间')),
                ('is_pass', models.BooleanField(default=False, verbose_name='评论是否审核通过')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='operation.Order', verbose_name='商家')),
            ],
            options={
                'verbose_name': '订单评论',
                'verbose_name_plural': '订单评论',
            },
        ),
    ]