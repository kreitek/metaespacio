# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('espacios', '0007_espacio_cuotas'),
    ]

    operations = [
        migrations.AddField(
            model_name='espacio',
            name='cuota_minima',
            field=models.FloatField(null=True),
        ),
    ]
