# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mortgage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('credit_limit', models.DecimalField(max_digits=8, decimal_places=2)),
                ('initial_balance', models.DecimalField(max_digits=8, decimal_places=2)),
                ('start_date', models.DateField(verbose_name=b'start date')),
                ('initial_rate', models.DecimalField(max_digits=6, decimal_places=2)),
                ('term', models.IntegerField(verbose_name=b'duration in months')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.DecimalField(max_digits=8, decimal_places=2)),
                ('type', models.CharField(max_length=200)),
                ('date', models.DateField(verbose_name=b'transaction date')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
    ]
