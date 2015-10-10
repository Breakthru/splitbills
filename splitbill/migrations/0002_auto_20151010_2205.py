# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('splitbill', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=16)),
            ],
        ),
        migrations.AlterField(
            model_name='transaction',
            name='tags',
            field=models.ManyToManyField(to='splitbill.Tag', blank=True),
        ),
    ]
