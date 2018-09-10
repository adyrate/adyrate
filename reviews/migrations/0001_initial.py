# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-13 18:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0002_clients'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.FloatField()),
                ('food_quality', models.FloatField()),
                ('value_for_money', models.FloatField()),
                ('hygiene', models.FloatField()),
                ('service', models.FloatField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.Clients')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.UsersAccount')),
            ],
        ),
        migrations.CreateModel(
            name='TransactionRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('credited_gs_points', models.IntegerField(default=0)),
                ('debited_gs_points', models.IntegerField(default=0)),
                ('before_discount', models.FloatField(default=0.0)),
                ('discount', models.FloatField(default=0.0)),
                ('after_discount', models.FloatField(default=0.0)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.Clients')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.UsersAccount')),
            ],
        ),
    ]
