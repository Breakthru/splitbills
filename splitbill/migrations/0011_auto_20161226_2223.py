# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-26 22:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('splitbill', '0010_auto_20161226_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statement',
            name='date_from',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='statement',
            name='date_to',
            field=models.DateField(blank=True, null=True),
        ),
    ]
