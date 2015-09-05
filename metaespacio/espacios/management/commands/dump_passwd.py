
from __future__ import unicode_literals
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from espacios.models import Espacio


class Command(BaseCommand):
    help = 'Dump passwd-like file for dokuwiki for example'

    def add_arguments(self, parser):
        parser.add_argument('espacio_slug')
        parser.add_argument('--dokuwiki', action='store_true', dest='dokuwiki', default=False, help='Print dokuwiki header')

    def handle(self, *args, **options):
        espacio = Espacio.objects.get(slug=options['espacio_slug'])

        if options['dokuwiki']:
            print "# users.auth.php"
            print "# <?php exit()?>"
            print "# Don't modify the lines above"
            print "#"
            print "# Userfile"
            print "#"
            print "# Format:"
            print "#"
            print "# login:passwordhash:Real Name:email:groups,comma,seperated"
            print 

        for u in User.objects.filter(espacio=espacio, is_active=True):
            perms = "admin,user" if u.is_superuser else "user"
            line = "{}:{}:{} {}:{}:{}".format(u.username, u.password,
                u.first_name, u.last_name, u.email, perms)
            print line.encode('utf-8')
