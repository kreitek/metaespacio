# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template import Library

register = Library()


@register.simple_tag
def asiento_resumen(asiento, prefijo=None):
    qs = asiento.linea_set.all()
    if prefijo:
        qs = qs.filter(cuenta__nombre__startswith=prefijo)
    cantidad = 0.0
    sumal = []
    sumar = []
    for l in qs:
        valor = l.cantidad
        if valor > 0:
            cantidad += l.cantidad
            sumar.append(l.cuenta.ultimo_nombre(prefijo))
        else:
            sumal.append(l.cuenta.ultimo_nombre(prefijo))
    return "{}->{} ({:.2f})".format(",".join(sumal), ",".join(sumar), cantidad)
