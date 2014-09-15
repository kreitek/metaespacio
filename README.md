MetaEspacio
===========

Django web app for management of (Hack/Maker/Cowork/Whatever/Meta)Spaces. The
main language of this project is spanish, but if you speak other language and
you think that this project could be useful to you in your language, please
contact us and we could join forces.

Aplicación web hecha en django para la gestión de
(Hack/Maker/Cowork/Loquesea/Meta)Espacios. El idioma principal del proyecto es
castellano, pero si hablas otro idioma y crees que este proyecto puede serte
util en tu idioma, por favor contáctcanos y podremos unir esfuerzos.


Instalation
===========

These django apps require django=1.6, which is the current stable.

If you use debian testing, you can install the dependencies using:

    apt-get install python-django # python-django-south

If you use virtualenv, you can install dependencies this way:

    apt-get install python-virtualenv
    virtualenv virtualenv
    . virtualenv/bin/activate
    pip install -r metaespacio/requirements.txt

As far as dependencies are installed, start the app with:

    cd metaespacio
    python manage.py syncdb
    python manage.py migrate
    python manage.py runserver
