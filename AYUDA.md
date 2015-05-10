Comandos utiles
===========

Crear un json de demo
cd metaespacio
. ../virtualenv/bin/activate
./manage.py dumpdata auth sites espacios pages encuestas cuotas --indent=1 > demo.json
