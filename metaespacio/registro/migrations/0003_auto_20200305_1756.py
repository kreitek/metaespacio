# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0002_auto_20150510_2008'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mac',
            name='user',
        ),
        migrations.DeleteModel(
            name='Mac',
        ),
    ]
