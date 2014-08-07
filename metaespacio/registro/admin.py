from django.contrib import admin

from .models import EspacioUser
from django.contrib.auth.models import User

class EspacioUserAdmin(admin.ModelAdmin):
    pass

admin.site.unregister(User)
admin.site.register(EspacioUser, EspacioUserAdmin)
