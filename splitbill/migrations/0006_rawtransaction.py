# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('splitbill', '0005_account_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='RawTransaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data', models.TextField()),
                ('date_added', models.DateTimeField()),
            ],
        ),
    ]
