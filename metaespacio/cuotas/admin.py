# -*- coding: utf-8 -*-

from django.contrib import admin
from . import models
from espacios.models import Espacio
from espacios.admin import EspacioAdmin


class MensualidadInline(admin.TabularInline):
    model = models.Mensualidad
    extra = 0


class PagoAdmin(admin.ModelAdmin):
    date_hierarchy = 'fecha'
    list_display = (
        '__unicode__', 'fecha', 'cantidad', 'numero_mensualidades', 'pagado_a')
    list_filter = ('forma_pago__espacio', )
    inlines = [MensualidadInline, ]

    def numero_mensualidades(self, obj):
        return obj.mensualidad_set.count()

    def pagado_a(self, obj):
        l = obj.mensualidad_set.values_list(
            'miembro__user__username', flat=True).distinct()
        return ", ".join(l)


admin.site.register(models.Pago, PagoAdmin)


class CuotaPeriodicaInline(admin.TabularInline):
    model = models.CuotaPeriodica
    extra = 0


class FormaPagoInline(admin.TabularInline):
    model = models.FormaPago
    extra = 0


class EspacioAdmin2(EspacioAdmin):
    inlines = EspacioAdmin.inlines + [FormaPagoInline, CuotaPeriodicaInline]

admin.site.unregister(Espacio)
admin.site.register(Espacio, EspacioAdmin2)
