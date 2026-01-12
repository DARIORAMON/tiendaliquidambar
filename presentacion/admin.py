from django.contrib import admin
from presentacion.models import CarrouselIntroduccion
from presentacion.models import ProductosDestacados
from presentacion.models import AireLibre
from presentacion.models import AireLibreBeneficios
from presentacion.models import Temporada
from presentacion.models import PreguntasFrecuentes


class TiendaCarrouselleadmin(admin.ModelAdmin):

    list_display = ["orden", "descripcion"]

    """def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False"""


class CarrouselIntroduccionadmin(admin.ModelAdmin):

    list_display = ["orden", "descripcion"]

    """def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False"""


class ProductosDestacadosadmin(admin.ModelAdmin):

    list_display = ["orden", "descripcion"]

    """def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False"""


class AireLibreBeneficiosInline(admin.TabularInline):

    model = AireLibreBeneficios
    extra = 0

    """def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False"""


class AireLibreadmin(admin.ModelAdmin):

    inlines = [AireLibreBeneficiosInline]

    """def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False"""


class Temporadaadmin(admin.ModelAdmin):

    list_display = ["titulo", "descripcion"]

    """def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False"""


class PortadaLineasadmin(admin.ModelAdmin):
    """def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False"""

    list_display = ["orden", "ruta", "titulo", "descripcion"]


class PreguntasFrecuentesAdmin(admin.ModelAdmin):
 
    list_display = ["pregunta"]


admin.site.register(CarrouselIntroduccion, CarrouselIntroduccionadmin)
admin.site.register(ProductosDestacados, ProductosDestacadosadmin)
admin.site.register(AireLibre, AireLibreadmin)
admin.site.register(Temporada, Temporadaadmin)
admin.site.register(PreguntasFrecuentes, PreguntasFrecuentesAdmin)
