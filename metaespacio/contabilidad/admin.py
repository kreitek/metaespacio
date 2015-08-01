from django.contrib import admin
from .models import Cuenta, Asiento, Linea


class LineaInline(admin.TabularInline):
    model = Linea
    extra = 2


class AsientoAdmin(admin.ModelAdmin):
    date_hierarchy = "fecha"
    list_display = ('fecha', 'concepto', 'lineas', )
    list_filter = ("espacio", "linea__cuenta")
    inlines = [LineaInline]

    def lineas(self, obj):
        return " ".join([unicode(x) for x in obj.linea_set.all()])


class CuentaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'espacio', 'signo')
    list_filter = ("espacio", )

admin.site.register(Asiento, AsientoAdmin)
admin.site.register(Cuenta, CuentaAdmin)
