# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('espacios', '0002_miembro_es_socio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Abono',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('miembro', models.ForeignKey(to='espacios.Miembro')),
            ],
        ),
        migrations.CreateModel(
            name='Taquilla',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('row', models.IntegerField()),
                ('col', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Taquillero',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('rows', models.IntegerField()),
                ('cols', models.IntegerField()),
                ('espacio', models.ForeignKey(to='espacios.Espacio')),
            ],
        ),
        migrations.AddField(
            model_name='taquilla',
            name='taquillero',
            field=models.ForeignKey(to='taquilla.Taquillero'),
        ),
        migrations.AddField(
            model_name='abono',
            name='taquilla',
            field=models.ForeignKey(to='taquilla.Taquilla'),
        ),
        migrations.AlterUniqueTogether(
            name='taquillero',
            unique_together=set([('espacio', 'name')]),
        ),
        migrations.AlterUniqueTogether(
            name='taquilla',
            unique_together=set([('taquillero', 'row', 'col')]),
        ),
    ]
