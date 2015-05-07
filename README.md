MetaEspacio
===========

Django web app for management of (Hack/Maker/Cowork/Whatever/Meta)Spaces. The
main language of this project is spanish, but if you speak other language and
you think that this project could be useful to you in your language, please
contact us and we could join forces.

Aplicación web hecha en django para la gestión de
(Hack/Maker/Cowork/Loquesea/Meta)Espacios.

Nosotros lo vamos a usar de forma intensiva en el Andén Sin Límite. Si dispones
de un espacio en Tenerife, tenemos que hablar, puesto que con esto, además de
facilitar tu organización, podemos beneficiarnos todos con servicios
transversales (para empezar el inicio de sesión unificado). Ya tenemos
implementadas las encuestas, y esperamos desarrollar la gestión de cuotas de
asociados, control de acceso de instalaciones (pestilleras electrónicas), y
herramientas de autogestión, como pueden ser wikis, grupos de trabajo.

Todo esto es software libre, Affero GPL, si quieres te lo instalas tu, pero el
beneficio está en cooperar.  No obstante, si acabas instalándolo y usándolo,
avísanos, pues no nos vamos a preocupar mantener actualizaciones limpias, hasta
que alguien nos avise, y vamos a estar sacando características nuevas todo el
rato... somos un hackerspace ;-)

El idioma principal del proyecto es castellano, pero si hablas otro idioma y
crees que este proyecto puede serte util en tu idioma, por favor contáctcanos y
podremos unir esfuerzos.


Instalation
===========

These django apps require django=1.8, which is the current stable.

When using virtualenv, you can install dependencies this way:

    apt-get install python-virtualenv python-dev libjpeg-dev libfreetype6-dev
    virtualenv virtualenv
    . virtualenv/bin/activate
    pip install -r metaespacio/requirements.txt
    pip install -r metaespacio/requirements_dev.txt

As far as dependencies are installed, start the app with:

    cd metaespacio
    python manage.py makemigrations  # normally does nothing
    python manage.py migrate
    python manage.py loaddata demo.json  # creates admin/admin and user/user and some data
    touch metaespacio/settings_local.py
    python manage.py runserver
