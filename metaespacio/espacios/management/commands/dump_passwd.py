
from __future__ import unicode_literals
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from espacios.models import Espacio


class Command(BaseCommand):
    help = 'Dump passwd-like file for dokuwiki for example'

    def add_arguments(self, parser):
        parser.add_argument('espacio_slug')

    def handle(self, *args, **options):
        espacio = Espacio.objects.get(slug=options['espacio_slug'])
        for u in User.objects.filter(espacio=espacio, is_active=True):
            perms = "admin,user" if u.is_superuser else "user"
            line = "{}:{}:{} {}:{}:{}".format(u.username, u.password,
                u.first_name, u.last_name, u.email, perms)
            print line.encode('utf-8')
