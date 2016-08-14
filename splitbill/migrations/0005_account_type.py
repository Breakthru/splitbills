# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('splitbill', '0004_auto_20160814_1410'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='type',
            field=models.CharField(default='TESCO', max_length=255),
            preserve_default=False,
        ),
    ]
