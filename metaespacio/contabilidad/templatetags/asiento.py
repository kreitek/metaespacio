# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template import Library

register = Library()


@register.simple_tag
def asiento_resumen(asiento, prefijo=None):
    qs = asiento.linea_set.all()
    if prefijo:
        qs = qs.filter(cuenta__nombre__startswith=prefijo)
    conceptos1, cantidades1 = [], []
    conceptos2, cantidades2 = [], []
    for l in qs:
        if l.cantidad < 0:
            conceptos1.append(l.cuenta.ultimo_nombre(prefijo))
            cantidades1.append(l.cantidad)
        elif l.cantidad > 0:
            conceptos2.append(l.cuenta.ultimo_nombre(prefijo))
            cantidades2.append(l.cantidad)
    if len(conceptos1) == len(conceptos2) == 1:
        return "{}->{}({:.2f})".format(
            ",".join(conceptos1),
            ",".join(conceptos2),
            cantidades2[0])
    else:
        return "{}({}) -> {}({})".format(
            ",".join(conceptos1),
            "+".join(["{:.2f}".format(-x) for x in cantidades1]),
            ",".join(conceptos2),
            "+".join(["{:.2f}".format(x) for x in cantidades2]),
            )
