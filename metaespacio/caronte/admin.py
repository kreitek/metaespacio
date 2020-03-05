from django.contrib import admin

from .models import Lector, Autorizacion, EntradaSalida


class LectorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'slug', 'espacio', 'last_uptime')


class AutorizacionAdmin(admin.ModelAdmin):
    list_display = ('user', 'codigo')


class EntradaSalidaAdmin(admin.ModelAdmin):
    # date_hierarchy = 'entrada'
    list_display = ('user', 'espacio', 'entrada', 'salida')
    list_filter = ('espacio', 'salida')
    readonly_fields = ('entrada', )


admin.site.register(Lector, LectorAdmin)
admin.site.register(Autorizacion, AutorizacionAdmin)
admin.site.register(EntradaSalida, EntradaSalidaAdmin)
