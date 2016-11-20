# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('espacios', '0009_auto_20161022_2318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='espacio',
            name='cuotas',
            field=models.ManyToManyField(related_name='cuenta_de', to='contabilidad.Cuenta'),
        ),
    ]
