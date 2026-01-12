from django.contrib import admin
from usuario.models import Perfil

class Perfiladmin(admin.ModelAdmin):
    list_display = ["usuario", "nombre", "apellido", "clave"]

admin.site.register(Perfil, Perfiladmin)
