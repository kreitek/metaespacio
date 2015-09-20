
from __future__ import unicode_literals
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from espacios.models import Espacio
from oidc_provider.models import UserInfo


class Command(BaseCommand):
    help = 'Create UserInfo data for login with openid (drupal)'

    def add_arguments(self, parser):
        parser.add_argument('espacio_slug')

    def handle(self, *args, **options):

        espacio = Espacio.objects.get(slug=options['espacio_slug'])
        users = User.objects.filter(espacio=espacio, is_active=True)

        for user in users:
            username = user.username.lower()
            if UserInfo.objects.filter(user=user).exists():
                print "Skipping {}".format(username)
            else:
                ui = UserInfo.objects.create(
                    user=user,
                    birthdate="1970-01-01",
                    gender="M",  # male
                    preferred_username=username,
                )
                print "Created {} for {}".format(ui, username)
