# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import espacios.models


class Migration(migrations.Migration):

    dependencies = [
        ('espacios', '0003_auto_20150507_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='espacio',
            name='logo',
            field=models.ImageField(null=True, upload_to=espacios.models.upload_to, blank=True),
        ),
    ]
