# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-09 13:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0011_auto_20180909_1140'),
    ]

    operations = [
        migrations.RenameField(
            model_name='redeemtransaction',
            old_name='client',
            new_name='store',
        ),
    ]
