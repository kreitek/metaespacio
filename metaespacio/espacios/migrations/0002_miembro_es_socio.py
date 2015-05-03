# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('espacios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='miembro',
            name='es_socio',
            field=models.BooleanField(default=False),
        ),
    ]
