# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagina',
            name='menu',
            field=models.CharField(help_text='Si quieres que salga en el men\xfa, pon el nombre aqui', max_length=255, null=True, blank=True),
        ),
    ]
