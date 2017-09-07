# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-06 13:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DrinkData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.CharField(default=b'USER', max_length=30)),
                ('time', models.DateTimeField(auto_now_add=True, null=True)),
                ('dose', models.FloatField(default=b'0')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('account', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=32)),
                ('userName', models.CharField(default=models.CharField(max_length=20, primary_key=True, serialize=False), max_length=32)),
                ('phoneNumber', models.CharField(max_length=11, null=True)),
                ('emailAddress', models.CharField(max_length=32, null=True)),
                ('height', models.FloatField(null=True)),
                ('wight', models.FloatField(null=True)),
                ('age', models.IntegerField(null=True)),
                ('gender', models.CharField(max_length=5, null=True)),
                ('registerTime', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
