from __future__ import unicode_literals
from django.contrib import admin
from django.core.urlresolvers import reverse
from django.utils.safestring import mark_safe
from .models import Cuenta, Asiento, Linea


class LineaInline(admin.TabularInline):
    model = Linea
    extra = 2


class AsientoAdmin(admin.ModelAdmin):
    date_hierarchy = "fecha"
    list_display = ('fecha', 'concepto', 'lineas', 'correcto')
    list_filter = ("espacio", "linea__cuenta")
    inlines = [LineaInline]

    def lineas(self, obj):
        url = reverse("admin:contabilidad_asiento_changelist")
        show = lambda x: '{:.2f} <a href="{}?linea__cuenta__id__exact={}">{}</a>'.format(
            x.cantidad, url, x.cuenta.id, x.cuenta.nombre)
        return mark_safe("<br/>".join([show(x) for x in obj.linea_set.all()]))

    def correcto(self, obj):
        d = obj.diferencia()
        return "OK" if abs(d) < 0.01 else d


class CuentaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'espacio', 'signo')
    list_filter = ("espacio", )

admin.site.register(Asiento, AsientoAdmin)
admin.site.register(Cuenta, CuentaAdmin)
