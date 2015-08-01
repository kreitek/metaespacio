# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('espacios', '0006_auto_20150510_2102'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asiento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('concepto', models.CharField(max_length=255)),
                ('fecha', models.DateField()),
                ('espacio', models.ForeignKey(to='espacios.Espacio')),
            ],
        ),
        migrations.CreateModel(
            name='Cuenta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=255)),
                ('ver_miembros', models.BooleanField(default=True)),
                ('signo', models.CharField(default='+', max_length=1, choices=[('+', '+'), ('-', '-')])),
                ('espacio', models.ForeignKey(to='espacios.Espacio')),
            ],
            options={
                'ordering': ('espacio', 'nombre'),
            },
        ),
        migrations.CreateModel(
            name='Linea',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.FloatField()),
                ('fecha', models.DateField(null=True, blank=True)),
                ('asiento', models.ForeignKey(to='contabilidad.Asiento')),
                ('cuenta', models.ForeignKey(to='contabilidad.Cuenta')),
                ('miembro', models.ForeignKey(blank=True, to='espacios.Miembro', null=True)),
            ],
            options={
                'ordering': ('asiento', '-cantidad'),
            },
        ),
        migrations.AlterUniqueTogether(
            name='cuenta',
            unique_together=set([('espacio', 'nombre')]),
        ),
    ]
