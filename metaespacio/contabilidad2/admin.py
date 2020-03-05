from django.contrib import admin
from .models import Validacion, Registro, Categoria


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('espacio', 'nombre', 'ayuda')


@admin.register(Validacion)
class ValidacionAdmin(admin.ModelAdmin):
    list_display = ('espacio', 'nombre', 'es_donacion', 'es_metalico', 'es_oficial')


@admin.register(Registro)
class RegistroAdmin(admin.ModelAdmin):
    date_hierarchy = 'fecha_factura'
    fieldsets = (
        ('Datos de sesión', {
            'fields': ('espacio', 'miembro', 'fecha_formulario'),
        }),
        ('Datos de usuario', {
            'fields': ('concepto', 'fecha_factura', 'categoria', 'importe', 'es_donado', 'foto', 'factura'),
        }),
        ('Datos de contabilidad', {
            'fields': ('validacion', 'fecha_pago', 'notas'),
        }),
    )
    list_display = ('fecha_', 'concepto', 'categoria_', 'importe', 'miembro')
    list_filter = ('espacio', 'categoria', 'miembro')
    search_fields = ('concepto', )
    readonly_fields = ('fecha_formulario', )

    def fecha_(self, obj):
        return obj.fecha_factura.strftime("%d/%m/%y")

    def categoria_(self, obj):
        return obj.categoria.nombre
