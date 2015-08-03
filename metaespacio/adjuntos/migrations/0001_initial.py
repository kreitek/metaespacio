# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import adjuntos.models


class Migration(migrations.Migration):

    dependencies = [
        ('contabilidad', '0003_auto_20150802_2009'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdjuntoAsiento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fichero', models.FileField(upload_to=adjuntos.models._upload_to)),
                ('asiento', models.ForeignKey(to='contabilidad.Asiento')),
            ],
        ),
    ]
