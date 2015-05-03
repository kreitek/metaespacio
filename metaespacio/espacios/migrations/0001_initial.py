# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Espacio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=60)),
                ('slug', models.CharField(max_length=60)),
                ('logo', models.ImageField(upload_to='logos')),
                ('facebook_fanpage', models.URLField(null=True, blank=True)),
                ('facebook_group', models.URLField(null=True, blank=True)),
                ('google_plus', models.URLField(null=True, blank=True)),
                ('google_group', models.URLField(null=True, blank=True)),
                ('youtube', models.URLField(null=True, blank=True)),
                ('twitter', models.URLField(null=True, blank=True)),
                ('www', models.URLField(null=True, blank=True)),
                ('blog', models.URLField(null=True, blank=True)),
                ('google_site', models.URLField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Miembro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_alta', models.DateField(auto_now=True)),
                ('espacio', models.ForeignKey(to='espacios.Espacio')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='espacio',
            name='miembros',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, through='espacios.Miembro'),
        ),
        migrations.AddField(
            model_name='espacio',
            name='site',
            field=models.ForeignKey(to='sites.Site'),
        ),
    ]
