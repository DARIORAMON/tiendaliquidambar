from django.contrib import admin
from productos.models.categoria import Categoria
from productos.models.producto import Producto
from productos.models.producto import ImagenProducto

# ************************************************
# * CATEGORIA
# ************************************************
class Categoriaadmin(admin.ModelAdmin):

    list_display = ["nombre", "slug", "orden" ]
    list_filter = ["nombre"]

# ************************************************
# * PRODUTOS
# ************************************************
class ImagenProductoInline(admin.TabularInline):

    model = ImagenProducto
    extra = 0

class Productoadmin(admin.ModelAdmin):
    fieldsets = [
        ("Relación", {"fields": ["categoria"]}),
        ("ARTICULO", {"fields": ["articulo"]}),
        ("PESO", {"fields": ["peso"]}),
        (
            "Datos generales",
            {
                "fields": [
                    "name",
                    # "nombre",
                    # "slug",
                    "imagen",
                    "descripcion",
                    "composicion",

                ]
            },
        ),
        (
            "Datos Monetarios",
            {"fields": ["precio", "descuento", "stock"]},
        ),
        ("Condición", {"fields": ["estado"]}),
    ]
    list_display = [
        "articulo",
        "name",
        "peso",
        "slug",
        "estado_de_producto",
        "categorias_del_producto",
    ]
    list_filter = ["name", ]

    inlines = [ImagenProductoInline,]
    readonly_fields = ("estado",)
    actions = [
        "publicar",
        "pasar_a_borrador",
        "pasar_a_retirado",
    ]


    def publicar(self, request, queryset):
        queryset.update(estado="Publicado")

    publicar.short_description = "Pasar a estado Publicado"

    def pasar_a_borrador(self, request, queryset):
        queryset.update(estado="Borrador")

    pasar_a_borrador.short_description = "Pasar a estado Borrador"

    def pasar_a_retirado(self, request, queryset):
        queryset.update(estado="Retirado")

    pasar_a_retirado.short_description = "Pasar a estado Retirado"

# ========= VAN COMENTADAS INICIO ===========================================
admin.site.register(Categoria, Categoriaadmin)
# ========= VAN COMENTADAS FIN ===========================================
admin.site.register(Producto, Productoadmin)
