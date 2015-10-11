# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offset', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
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
        migrations.AddField(
            model_name='transaction',
            name='mtg',
            field=models.ForeignKey(default=1, to='offset.Mortgage'),
            preserve_default=False,
        ),
    ]
