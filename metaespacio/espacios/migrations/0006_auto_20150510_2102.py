# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import espacios.models


class Migration(migrations.Migration):

    dependencies = [
        ('espacios', '0005_espacio_favicon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='espacio',
            name='favicon',
            field=models.ImageField(help_text='El formato debe ser PNG y tama\xf1o 16x16 o 32x32', null=True, upload_to=espacios.models.favicons_upload_to, blank=True),
        ),
    ]
