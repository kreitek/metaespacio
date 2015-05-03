# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('espacios', '0002_miembro_es_socio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Encuesta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_creacion', models.DateTimeField()),
                ('fecha_finalizacion', models.DateTimeField(null=True, blank=True)),
                ('pregunta', models.CharField(max_length=255)),
                ('texto', models.TextField(blank=True)),
                ('voto_anonimo', models.BooleanField()),
                ('voto_multiple', models.BooleanField()),
                ('voto_editable', models.BooleanField()),
                ('espacio', models.ForeignKey(to='espacios.Espacio')),
            ],
        ),
        migrations.CreateModel(
            name='Opcion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('eleccion', models.CharField(max_length=255)),
                ('texto', models.TextField(blank=True)),
                ('encuesta', models.ForeignKey(to='encuestas.Encuesta')),
            ],
        ),
        migrations.CreateModel(
            name='Voto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.DateTimeField(auto_now=True)),
                ('miembro', models.ForeignKey(to='espacios.Miembro')),
                ('opcion', models.ForeignKey(to='encuestas.Opcion')),
            ],
        ),
    ]
