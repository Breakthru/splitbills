# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offset', '0002_auto_20151011_1215'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(verbose_name=b'instruction date')),
                ('type', models.CharField(max_length=200)),
                ('amount', models.DecimalField(max_digits=8, decimal_places=2)),
                ('mtg', models.ForeignKey(to='offset.Mortgage')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.RemoveField(
            model_name='orders',
            name='mtg',
        ),
        migrations.DeleteModel(
            name='Orders',
        ),
    ]
