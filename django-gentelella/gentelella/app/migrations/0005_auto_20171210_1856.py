# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-10 18:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20171209_2339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ip',
            name='endereco_ip',
            field=models.CharField(max_length=15, unique=True),
        ),
        migrations.AlterField(
            model_name='iptables',
            name='total_pacotes',
            field=models.IntegerField(unique=True),
        ),
    ]
