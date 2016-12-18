# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('splitbill', '0006_rawtransaction'),
    ]

    operations = [
        migrations.CreateModel(
            name='RawLabels',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag', models.ForeignKey(to='splitbill.Tag')),
                ('transaction', models.ForeignKey(to='splitbill.RawTransaction')),
            ],
        ),
    ]
