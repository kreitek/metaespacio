# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_pagina_menu'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pagina',
            options={'ordering': ('espacio', 'orden'), 'verbose_name': 'p\xe1gina'},
        ),
    ]
