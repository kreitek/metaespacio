# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Espacio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='MiembroEspacio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_alta', models.DateTimeField(auto_now=True)),
                ('espacio', models.ForeignKey(to='espacios.Espacio')),
                ('usuario', models.ForeignKey(to='registro.Usuario')),
            ],
        ),
        migrations.AddField(
            model_name='espacio',
            name='miembros',
            field=models.ManyToManyField(to='registro.Usuario', through='espacios.MiembroEspacio'),
        ),
    ]
