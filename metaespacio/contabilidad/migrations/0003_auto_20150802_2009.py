# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contabilidad', '0002_auto_20150802_1925'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='linea',
            options={'ordering': ('asiento', '-cantidad', '-fecha')},
        ),
    ]
