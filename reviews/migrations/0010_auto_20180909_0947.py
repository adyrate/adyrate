# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-09 09:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0009_auto_20180907_1640'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coupons',
            old_name='points_cost',
            new_name='ady_points_cost',
        ),
    ]
