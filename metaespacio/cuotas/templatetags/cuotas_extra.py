from cuotas.models import Pago
from django.template import Library

register = Library()

@register.simple_tag
def get_str_tipo(tipo_number):
    d = {x[0]:x[1] for x in Pago.tiposDePago}
    return d[int(tipo_number)]