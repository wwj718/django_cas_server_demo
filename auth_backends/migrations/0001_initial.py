# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-29 07:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SeuUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=128)),
            ],
        ),
    ]
