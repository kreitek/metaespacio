# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contabilidad', '0003_auto_20150802_2009'),
        ('espacios', '0006_auto_20150510_2102'),
    ]

    operations = [
        migrations.AddField(
            model_name='espacio',
            name='cuotas',
            field=models.OneToOneField(related_name='cuenta_de', null=True, to='contabilidad.Cuenta'),
        ),
    ]
