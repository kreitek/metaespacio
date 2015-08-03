from django.contrib import admin
from contabilidad.models import Asiento
from contabilidad.admin import AsientoAdmin
from adjuntos.models import AdjuntoAsiento


class AdjuntoInline(admin.TabularInline):
    model = AdjuntoAsiento
    extra = 0


class AsientoAdminNew(AsientoAdmin):
    inlines = AsientoAdmin.inlines + [AdjuntoInline]

admin.site.unregister(Asiento)
admin.site.register(Asiento, AsientoAdminNew)
