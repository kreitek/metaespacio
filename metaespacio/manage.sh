#!/bin/sh

log () {
    echo ----------------------------------------------------------------------
    echo $*
}

set -e

test -e .virtualenv || {
    log creando .virtualenv
    virtualenv .virtualenv --python=python3
}

log Activando .virtualenv
. .virtualenv/bin/activate

log Instalando .virtualenv
pip install -r requirements.txt 

# log "Safety check (un mes)"
# pip install safety
# pip freeze | safety check --bare

log Aplicando migraciones
./manage.py migrate

SUPERUSERS=$(./manage.py shell -c 'from django.contrib.auth.models import User; print(User.objects.filter(is_superuser=True).count())')
test $SUPERUSERS = 0 && {
    log Creando superusuario
    ./manage.py createsuperuser --username admin --email root@galotecnia.com --noinput
}

log ./manage.py check
./manage.py check

log ./manage.py $*
./manage.py $*

