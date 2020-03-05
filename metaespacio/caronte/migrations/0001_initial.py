# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('espacios', '0010_auto_20161023_1130'),
    ]

    operations = [
        migrations.CreateModel(
            name='Autorizacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(unique=True, max_length=20)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EntradaSalida',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('entrada', models.DateTimeField(auto_now_add=True)),
                ('salida', models.DateTimeField(null=True, blank=True)),
                ('espacio', models.ForeignKey(to='espacios.Espacio')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Lector',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255)),
                ('last_uptime', models.DateTimeField(null=True, blank=True)),
                ('espacio', models.ForeignKey(to='espacios.Espacio')),
            ],
            options={
                'verbose_name_plural': 'lectores',
            },
        ),
    ]
