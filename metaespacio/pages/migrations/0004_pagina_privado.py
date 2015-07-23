# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20150510_2021'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagina',
            name='privado',
            field=models.BooleanField(default=False),
        ),
    ]
