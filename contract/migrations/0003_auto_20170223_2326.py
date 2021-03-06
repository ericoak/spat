# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-23 23:26
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contract', '0002_auto_20170223_1124'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='supplier',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='contract.Supplier'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contact',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 23, 23, 26, 28, 887370)),
        ),
        migrations.AlterField(
            model_name='contact',
            name='viewed',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 23, 23, 26, 28, 887438)),
        ),
        migrations.AlterField(
            model_name='contract',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 23, 23, 26, 28, 889716)),
        ),
        migrations.AlterField(
            model_name='contract',
            name='viewed',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 23, 23, 26, 28, 889765)),
        ),
        migrations.AlterField(
            model_name='note',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 23, 23, 26, 28, 890908)),
        ),
        migrations.AlterField(
            model_name='note',
            name='viewed',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 23, 23, 26, 28, 890960)),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 23, 23, 26, 28, 888638)),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='viewed',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 23, 23, 26, 28, 888691)),
        ),
    ]
