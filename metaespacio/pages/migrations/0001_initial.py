# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('espacios', '0002_miembro_es_socio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pagina',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('orden', models.IntegerField(default=0)),
                ('slug', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('espacio', models.ForeignKey(to='espacios.Espacio')),
            ],
            options={
                'ordering': ('espacio', 'orden'),
            },
        ),
        migrations.AlterUniqueTogether(
            name='pagina',
            unique_together=set([('espacio', 'slug')]),
        ),
    ]
