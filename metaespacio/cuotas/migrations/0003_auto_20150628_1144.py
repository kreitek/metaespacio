# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cuotas', '0002_auto_20150628_1132'),
    ]

    operations = [
        migrations.AddField(
            model_name='formapago',
            name='color',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='formapago',
            name='posicion',
            field=models.IntegerField(default=0),
        ),
    ]
