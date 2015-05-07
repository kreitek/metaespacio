# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('espacios', '0002_miembro_es_socio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='espacio',
            name='logo',
            field=models.ImageField(null=True, upload_to='logos', blank=True),
        ),
    ]
