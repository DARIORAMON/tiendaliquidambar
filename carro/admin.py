from django.contrib import admin
from .models import ConfiguracionEnvio

@admin.register(ConfiguracionEnvio)
class ConfiguracionEnvioAdmin(admin.ModelAdmin):
    list_display = ('codigo_postal_base', 'localidad', 'provincia', 'tarifa_por_km')
