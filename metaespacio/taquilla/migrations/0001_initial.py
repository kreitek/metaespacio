# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AbonoTaquilla',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
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
            ],
        ),
        migrations.AddField(
            model_name='taquilla',
            name='taquillero',
            field=models.ForeignKey(to='taquilla.Taquillero'),
        ),
        migrations.AddField(
            model_name='abonotaquilla',
            name='taquilla',
            field=models.ForeignKey(to='taquilla.Taquilla'),
        ),
    ]
