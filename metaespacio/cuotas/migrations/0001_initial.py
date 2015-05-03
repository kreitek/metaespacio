# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('espacios', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='CuotaPeriodica',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.FloatField()),
                ('fecha_inicial', models.DateField()),
                ('fecha_final', models.DateField(null=True, blank=True)),
                ('espacio', models.ForeignKey(to='espacios.Espacio')),
            ],
            options={
                'verbose_name': 'cuota peri\xf3dica',
                'verbose_name_plural': 'cuotas peri\xf3dicas',
            },
        ),
        migrations.CreateModel(
            name='FormaPago',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=255, null=True, blank=True)),
                ('porcentaje_comision', models.FloatField(default=0.0)),
                ('espacio', models.ForeignKey(to='espacios.Espacio')),
            ],
            options={
                'verbose_name': 'forma de pago',
                'verbose_name_plural': 'formas de pago',
            },
        ),
        migrations.CreateModel(
            name='Mensualidad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField(null=True, blank=True)),
                ('cantidad', models.FloatField()),
                ('miembro', models.ForeignKey(to='espacios.Miembro')),
            ],
            options={
                'ordering': ('fecha',),
                'verbose_name': 'mensualidad',
                'verbose_name_plural': 'mensualidades',
            },
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField()),
                ('cantidad', models.FloatField()),
                ('description', models.CharField(max_length=255, null=True, blank=True)),
                ('forma_pago', models.ForeignKey(to='cuotas.FormaPago')),
                ('pagador', models.ForeignKey(blank=True, to='espacios.Miembro', null=True)),
            ],
            options={
                'ordering': ('fecha',),
            },
        ),
        migrations.AddField(
            model_name='mensualidad',
            name='pago',
            field=models.ForeignKey(to='cuotas.Pago'),
        ),
    ]
