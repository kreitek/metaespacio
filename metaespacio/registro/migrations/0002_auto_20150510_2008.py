# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import registro.models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datospersonales',
            name='avatar',
            field=models.ImageField(upload_to=registro.models.upload_to),
        ),
    ]
