# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cuotas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='formapago',
            name='comision_fija',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='formapago',
            name='liquido',
            field=models.BooleanField(default=True),
        ),
    ]
