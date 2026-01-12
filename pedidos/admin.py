from django.contrib import admin
from pedidos.models import Pedido
from pedidos.models import Item
from pedidos.models import EnviarFactura


class ItemInline(admin.TabularInline):

    model = Item
    raw_id_fields = ["cada_producto"]  #esto es porque no quiero una lista de productos, solo el id del producto
    extra = 0
    """readonly_fields = [
        "usuario",
        "producto",
        "cantidad",
        "precio",
         
    ]"""

    def has_change_permission(self, request, obj=None):
        return False

class EnviarFacturaInline(admin.TabularInline):

    model = EnviarFactura
    extra = 0


class Pedidoadmin(admin.ModelAdmin):

 
    fieldsets = [
        (
            "Datos del pedido",
            {
                "fields": [
                    "tipo_transporte",
                    "referencia",
                    "estado_de_pedido",
                    
                    "total",
                    "total_mas_envio",
                    "created",
                    "modified",
                ]
            },
        ),
        (
            "Datos del comprador",
            {
                "fields": [
                    "usuario",
                    "documento",
                    "email",
                    "nombre",
                    "apellido",
                    "domicilio",
                    "provincia",
                    "localidad",
                    "codigo_postal",
                    "telefono",
                    "mensaje",
                ]
            },
        ),
        (
            "Datos del Destinatario",
            {
                "fields": [
                    "nombre_apellido_recibe",  
                    "documento_recibe",  
                    "domicilio_recibe", 
                    "localidad_recibe", 
                    "provincia_recibe",
                    "codigo_postal_recibe", 
                    "telefono_recibe",
                ]
            },
        ),

        (
            "Factura A / E",
            {
                "fields": [
                    "cuil_cuit",
                    "condicion_afip",
                    "razon_social",
                    "domicilio_comercial",
                ]
            },
        ),   
    ]
    list_display = [
        "tipo_transporte",
        "referencia",
        "estado_de_pedido",        
        "total",
        "total_mas_envio",
        "usuario",
        "nombre",
        "apellido",
        "cuil_cuit",
        "domicilio",
        "provincia",
        "localidad",
        "codigo_postal",
        "telefono",
        "documento",
        "mensaje",
        # "fecha",
        "email",
        "created",
        "modified",
    ]
    readonly_fields = [
        #"cada_producto",
        #"tipo_transporte",
        #"referencia",
        "estado_de_pedido",
        #"total",
        #"total_mas_envio",
        "usuario",
        "nombre",
        "apellido",
        "cuil_cuit",
        #"condicion_afip",
        #"razon_social",
        #"domicilio_comercial",
        #"documento",
        "domicilio",
        "provincia",
        "localidad",
        "codigo_postal",
        "telefono",
        "documento",
        #"mensaje",
        # "fecha",
        #"email",
        "created",
        "modified",
        #"nombre_apellido_recibe",  
        #"documento_recibe",  
        #"domicilio_recibe", 
        #"localidad_recibe", 
        #"provincia_recibe",
        #"codigo_postal_recibe", 
        #"telefono_recibe",


    ]

    list_filter = [
        "estado",
        "created",
        "modified",
    ]  # "fecha"

    search_fields = ["nombre", "email", "documento"]
    inlines = [ItemInline, EnviarFacturaInline]
    

    actions = ["pedido_enviado", "pedido_acreditado", "pedido_no_acreditado", "pedido_facturado"]

    def pedido_enviado(self, request, queryset):
        queryset.update(estado="DESPACHADO")
    pedido_enviado.short_description = "Marcar como Despachado"

    def pedido_acreditado(self, request, queryset):
        queryset.update(estado="ACREDITADO")
    pedido_acreditado.short_description = "Marcar como Acreditado"

    def pedido_no_acreditado(self, request, queryset):
        queryset.update(estado="NO ACREDITADO")
    pedido_no_acreditado.short_description = "Marcar como No Acreditado"

    def pedido_facturado(self, request, queryset):
        queryset.update(estado="FACTURADO")
    pedido_facturado.short_description = "Marcar como Facturado"


admin.site.register(Pedido, Pedidoadmin)

