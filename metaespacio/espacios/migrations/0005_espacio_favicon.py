# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import espacios.models


class Migration(migrations.Migration):

    dependencies = [
        ('espacios', '0004_auto_20150510_2008'),
    ]

    operations = [
        migrations.AddField(
            model_name='espacio',
            name='favicon',
            field=models.ImageField(null=True, upload_to=espacios.models.favicons_upload_to, blank=True),
        ),
    ]
