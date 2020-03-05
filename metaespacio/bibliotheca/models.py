from django.conf import settings
from django.db import models
from django.utils import timezone


class Author(models.Model):
    id_author = models.AutoField(primary_key=True)
    given_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=22, blank=True)
    surname = models.CharField(max_length=70)

    def __str__(self):
        if self.middle_name:
            return '{} {}. {}'.format(self.given_name, self.middle_name[0], self.surname)
        else:
            return '{} {}'.format(self.given_name, self.surname)

    class Meta:
        db_table = 'bib_author'
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'


class Publisher(models.Model):
    id_publisher = models.AutoField(primary_key=True)
    publisher_name = models.CharField(max_length=400)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.publisher_name

    class Meta:
        db_table = 'bib_publisher'
        verbose_name = 'Editorial'
        verbose_name_plural = 'Editoriales'


_LANGUAGES = (
    ('sp', 'Español'),
    ('en', 'Inglés'),
)


class Book(models.Model):

    class Meta:
        db_table = 'bib_book'
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'

    id_book = models.AutoField(primary_key=True)
    title = models.CharField(max_length=256)
    subtitle = models.CharField(max_length=512, blank=True)
    isbn = models.CharField(max_length=13)
    n_pages = models.IntegerField(default=0)
    digest = models.TextField(max_length=2048, blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    publisher = models.ForeignKey(Publisher)
    url = models.URLField(blank=True)
    cover = models.ImageField(upload_to='bibliotheca/book/cover', max_length=240,
                              blank=True)
    lang = models.CharField(max_length=2, choices=_LANGUAGES)
    entry_date = models.DateField(default=timezone.now)

    def __str__(self):
        return '{} (ISBN: {})'.format(self.title, self.isbn)


class Authorship(models.Model):
    id_authorship = models.AutoField(primary_key=True)
    book = models.ForeignKey(Book)
    author = models.ForeignKey(Author)
    rank = models.IntegerField(default=0)

    def __str__(self):
        return '{} wrote "{}"'.format(self.author, self.book.title)

    class Meta:
        db_table = 'bib_authorship'
        verbose_name = 'Autoría'
        verbose_name_plural = 'Autorías'
        unique_together = ('book', 'author',)
