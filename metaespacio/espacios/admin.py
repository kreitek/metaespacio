from django.contrib import admin
from .models import Espacio, Miembro
from django.contrib.auth.models import User
from registro.admin import UserAdmin2


class MiembroInline(admin.TabularInline):
    model = Miembro
    extra = 0


class EspacioAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'cuenta_miembros', 'site']
    inlines = [MiembroInline, ]

    def cuenta_miembros(self, obj):
        return obj.miembros.count()


class MiembroAdmin(admin.ModelAdmin):
    list_display = ['__unicode__', 'fecha_alta']
    list_filter = ['espacio']


class UserAdmin3(UserAdmin2):
    inlines = UserAdmin2.inlines + [MiembroInline]


admin.site.register(Espacio, EspacioAdmin)
admin.site.register(Miembro, MiembroAdmin)
admin.site.unregister(User)
admin.site.register(User, UserAdmin3)
