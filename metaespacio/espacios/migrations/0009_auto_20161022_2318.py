# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contabilidad', '0003_auto_20150802_2009'),
        ('espacios', '0008_espacio_cuota_minima'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='espacio',
            name='cuotas',
        ),
        migrations.AddField(
            model_name='espacio',
            name='cuotas',
            field=models.ManyToManyField(related_name='cuenta_de', null=True, to='contabilidad.Cuenta'),
        ),
    ]
