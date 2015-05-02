from django.contrib import admin

from .models import DatosPersonales
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin


class DatosPersonalesInline(admin.StackedInline):
    model = DatosPersonales


class UserAdmin2(UserAdmin):
    inlines = UserAdmin.inlines + [DatosPersonalesInline]


admin.site.unregister(User)
admin.site.register(User, UserAdmin2)
