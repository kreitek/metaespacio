# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cuotas', '0004_auto_20150705_1105'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoriapago',
            options={'ordering': ('posicion',), 'verbose_name': 'categor\xeda de pago', 'verbose_name_plural': 'categor\xedasde de pago'},
        ),
        migrations.AddField(
            model_name='pago',
            name='tipo',
            field=models.IntegerField(default=1, choices=[(1, 'Ingresos'), (2, 'Neutro'), (3, 'Gastos')]),
        ),
    ]
