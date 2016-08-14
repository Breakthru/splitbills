# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('splitbill', '0003_transaction_transaction_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Card',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='transaction_date',
        ),
        migrations.AddField(
            model_name='transaction',
            name='account',
            field=models.ForeignKey(default=0, to='splitbill.Account'),
            preserve_default=False,
        ),
    ]
