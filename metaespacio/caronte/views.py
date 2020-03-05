from django.contrib.auth.models import User
from django.http import HttpResponse

from .models import Lector, EntradaSalida


def lector_codigo(request, lector_slug, codigo):
    try:
        lector = Lector.objects.get(slug=lector_slug)
    except Lector.DoesNotExist:
        return HttpResponse("No existe lector")
    lector.uptime()
    try:
        usuario = User.objects.get(autorizacion__codigo=codigo)
    except User.DoesNotExist:
        return HttpResponse("No existe usuario")
    if lector.espacio not in usuario.espacio_set.all():
        return HttpResponse("Usuario no esta en espacio")
    qs = EntradaSalida.objects.filter(user=usuario, espacio=lector.espacio)
    last = qs.first()
    if not last:
        last = EntradaSalida.objects.create(user=usuario, espacio=lector.espacio)
        return HttpResponse("Bienvenido {}".format(usuario.username))
    elif not last.salida:
        last.sale()
        return HttpResponse("Adios {}".format(usuario.username))
    else:
        EntradaSalida.objects.create(user=usuario, espacio=lector.espacio)
        return HttpResponse("Bienvenido {}".format(usuario.username))


def lector_keepalive(request, lector_slug):
    try:
        lector = Lector.objects.get(slug=lector_slug)
    except Lector.DoesNotExist:
        return HttpResponse("KO")
    lector.uptime()
    return HttpResponse("OK")
