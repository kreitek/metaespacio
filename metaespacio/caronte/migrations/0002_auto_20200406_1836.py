# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caronte', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='autorizacion',
            options={'verbose_name': 'autorizaci\xf3n', 'verbose_name_plural': 'autorizaciones'},
        ),
        migrations.AlterModelOptions(
            name='entradasalida',
            options={'ordering': ['-entrada'], 'verbose_name': 'entrada y salida', 'verbose_name_plural': 'entradas y salidas'},
        ),
    ]
