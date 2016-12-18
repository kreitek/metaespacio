from __future__ import unicode_literals
from django.contrib import admin
from django.core.urlresolvers import reverse
from django.utils.safestring import mark_safe
from .models import Cuenta, Asiento, Linea


class LineaInline(admin.TabularInline):
    model = Linea
    extra = 2
    ordering = ("cuenta__nombre", "cantidad")


class AsientoAdmin(admin.ModelAdmin):
    date_hierarchy = "fecha"
    list_display = ('fecha', 'concepto', 'lineas', 'correcto', 'oficial')
    list_filter = ("espacio", "linea__miembro", "linea__cuenta")
    search_fields = ('concepto', )
    inlines = [LineaInline]

    def lineas(self, obj):
        url = reverse("admin:contabilidad_asiento_changelist")
        show = lambda x: '{:.2f} <a href="{}?linea__cuenta__id__exact={}">{}</a>'.format(
            x.cantidad, url, x.cuenta.id, x.cuenta.nombre)
        return mark_safe("<br/>".join([show(x) for x in obj.linea_set.all()]))

    def correcto(self, obj):
        return abs(obj.diferencia()) < 0.01
    correcto.boolean = True

    def oficial(self, obj):
        value = obj.diferencia("Oficial")
        if value is None:
            return None
        return abs(value) < 0.01
    oficial.boolean = True


class CuentaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'espacio', 'signo', 'ver_miembros')
    list_filter = ("espacio", 'signo', 'ver_miembros')

admin.site.register(Asiento, AsientoAdmin)
admin.site.register(Cuenta, CuentaAdmin)
