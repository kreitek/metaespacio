# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('espacios', '0006_auto_20150510_2102'),
        ('cuotas', '0003_auto_20150628_1144'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaPago',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=255, null=True, blank=True)),
                ('color', models.CharField(default='', max_length=30, blank=True)),
                ('posicion', models.IntegerField(default=0)),
                ('espacio', models.ForeignKey(to='espacios.Espacio')),
            ],
            options={
                'ordering': ('posicion',),
                'verbose_name': 'categor\xeda',
                'verbose_name_plural': 'categor\xedas',
            },
        ),
        migrations.AlterModelOptions(
            name='formapago',
            options={'ordering': ('posicion',), 'verbose_name': 'forma de pago', 'verbose_name_plural': 'formas de pago'},
        ),
        migrations.AlterField(
            model_name='formapago',
            name='color',
            field=models.CharField(default='', max_length=30, blank=True),
        ),
        migrations.AddField(
            model_name='mensualidad',
            name='categoria',
            field=models.ForeignKey(default=1, to='cuotas.CategoriaPago'),
        ),
    ]
