# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-25 01:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('splitbill', '0007_rawlabels'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rawtransaction',
            old_name='data',
            new_name='raw_data',
        ),
        migrations.AddField(
            model_name='rawtransaction',
            name='account',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='splitbill.Account'),
            preserve_default=False,
        ),
    ]