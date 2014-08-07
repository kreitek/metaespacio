from django.contrib import admin

from .models import Usuario
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _

class UsuarioAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (_('Extra fields'), {'fields': ('dni', 'direccion', 'telefono')}),
    )
    pass

admin.site.unregister(User)
admin.site.register(Usuario, UsuarioAdmin)
