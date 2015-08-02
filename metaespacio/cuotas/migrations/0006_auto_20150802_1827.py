# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cuotas', '0005_auto_20150705_1121'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mensualidad',
            options={'ordering': ('-fecha',), 'verbose_name': 'mensualidad', 'verbose_name_plural': 'mensualidades'},
        ),
    ]
