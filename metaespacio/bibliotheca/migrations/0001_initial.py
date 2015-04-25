# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id_author', models.AutoField(serialize=False, primary_key=True)),
                ('given_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(max_length=22, blank=True)),
                ('surname', models.CharField(max_length=70)),
            ],
            options={
                'db_table': 'bib_author',
                'verbose_name': 'Autor',
                'verbose_name_plural': 'Autores',
            },
        ),
        migrations.CreateModel(
            name='Authorship',
            fields=[
                ('id_authorship', models.AutoField(serialize=False, primary_key=True)),
                ('rank', models.IntegerField(default=0)),
                ('author', models.ForeignKey(to='bibliotheca.Author')),
            ],
            options={
                'db_table': 'bib_authorship',
                'verbose_name': 'Autor\xeda',
                'verbose_name_plural': 'Autor\xedas',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id_book', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=256)),
                ('subtitle', models.CharField(max_length=512, blank=True)),
                ('isbn', models.CharField(max_length=13)),
                ('n_pages', models.IntegerField(default=0)),
                ('digest', models.TextField(max_length=2048, blank=True)),
                ('url', models.URLField(blank=True)),
                ('cover', models.ImageField(max_length=240, upload_to=b'bibliotheca/book/cover', blank=True)),
                ('lang', models.CharField(max_length=2, choices=[(b'sp', b'Espa\xc3\xb1ol'), (b'en', b'Ingl\xc3\xa9s')])),
                ('entry_date', models.DateField(default=django.utils.timezone.now)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'bib_book',
                'verbose_name': 'Libro',
                'verbose_name_plural': 'Libros',
            },
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id_publisher', models.AutoField(serialize=False, primary_key=True)),
                ('publisher_name', models.CharField(max_length=400)),
                ('url', models.URLField(blank=True)),
            ],
            options={
                'db_table': 'bib_publisher',
                'verbose_name': 'Editorial',
                'verbose_name_plural': 'Editoriales',
            },
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(to='bibliotheca.Publisher'),
        ),
        migrations.AddField(
            model_name='authorship',
            name='book',
            field=models.ForeignKey(to='bibliotheca.Book'),
        ),
        migrations.AlterUniqueTogether(
            name='authorship',
            unique_together=set([('book', 'author')]),
        ),
    ]
