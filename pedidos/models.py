from django.db import models
from django.contrib.auth.models import User
from django.utils.html import format_html

from productos.models.producto import Producto

User._meta.get_field("email")._unique = True
from datetime import datetime
from model_utils.models import TimeStampedModel
from django.core.mail import EmailMessage

# class Pedido(models.Model):
class Pedido(TimeStampedModel):

    ESTADO_PEDIDO = [
        ("A CONFIRMAR", "A CONFIRMAR"),
        ("NO ACREDITADO", "NO ACREDITADO"),
        ("ACREDITADO", "ACREDITADO"),
        ("FACTURADO", "FACTURADO"),
        ("DESPACHADO", "DESPACHADO"),
    ]

    BSAS = "Buenos Aires"
    CABA = "Capital Federal"
    CATAMARCA = "Catamarca"
    CHACO = "Chaco"
    CHUBUT = "Chubut"
    CORDOBA = "Córdoba"
    CORRIENTES = "Corrientes"
    ENTRERIOS = "Entre Ríos"
    FORMOSA = "Formosa"
    JUJUY = "JujuY"
    LAPAMPA = "La Pampa"
    LARIOJA = "La Rioja"
    MENDOZA = "Mendoza"
    MISIONES = "Misiones"
    NEUQUEN = "Neuquén"
    RIONEGRO = "Río Negro"
    SALTA = "Salta"
    SANJUAN = "San Juan"
    SANLUIS = "San Luis"
    SANTACRUZ = "Santa Cruz"
    SANTAFE = "Santa Fe"
    SANTIADODELESTERO = "Santiago del Estero"
    TIERRADELFUEGO = "Tierra del Fuego"
    TUCUMAN = "Tucumán"

    PROVINCIA = (
        (BSAS, "Buenos Aires"),
        (CABA, "Capital Federal"),
        (CATAMARCA, "Catamarca"),
        (CHACO, "Chaco"),
        (CHUBUT, "Chubut"),
        (CORDOBA, "Córdoba"),
        (CORRIENTES, "Corrientes"),
        (ENTRERIOS, "Entre Ríos"),
        (FORMOSA, "Formosa"),
        (JUJUY, "Jujuy"),
        (LAPAMPA, "La Pampa"),
        (LARIOJA, "La Rioja"),
        (MENDOZA, "Mendoza"),
        (MISIONES, "Misiones"),
        (NEUQUEN, "Neuquén"),
        (RIONEGRO, "Río Negro"),
        (SALTA, "Salta"),
        (SANJUAN, "San Juan"),
        (SANLUIS, "San Luis"),
        (SANTACRUZ, "Santa Cruz"),
        (SANTAFE, "Santa Fe"),
        (SANTIADODELESTERO, "Santiago del Estero"),
        (TIERRADELFUEGO, "Tierra del Fuego"),
        (TUCUMAN, "Tucumán"),
    )

    TIPO_ENVIO = [
        ("EN FABRICA", "EN FABRICA"),
        ("A DOMICILIO", "A DOMICILIO"),
        ("A COORDINAR", "A COORDINAR"),
    ]
    RNO = "IVA Responsable No Inscripto"
    SE= "IVA Sujeto Exento"
    CF = "Consumidor Final"
    RM = "Responsable Monotributo"
    PE = "Proveedor del Exterior"
    CE = "Cliente del Exterior"
    IL = "IVA Liberado - Ley 19.640"
    MS = "Monotributista Social"
    IA = "IVA No Alcanzado"
    AFIP = (
        (RNO, "IVA Responsable No Inscripto"),
        (SE, "IVA Sujeto Exento"),
        (CF, "Consumidor Final"),
        (RM, "Responsable Monotributo"),
        (PE, "Proveedor del Exterior"),
        (CE, "Cliente del Exterior"),
        (IL, "IVA Liberado - Ley 19.640"),
        (MS, "Monotributista Social"),
        (IA, "IVA No Alcanzado"),
    )
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre = models.CharField(
        max_length=50,
    )
    apellido = models.CharField(
        max_length=50,
    )
    cuil_cuit = models.CharField(max_length=50, blank=True, null=True, default="---")
    domicilio = models.CharField(
        max_length=50,
    )
    localidad = models.CharField(
        max_length=50,
    )
    provincia = models.CharField(max_length=50, choices=PROVINCIA)
    codigo_postal = models.CharField(
        max_length=8, blank=True, null=True
    )
    telefono = models.CharField(max_length=15, blank=True, null=True)
    documento = models.CharField(
        max_length=20,
    )
    mensaje = models.TextField(default="")
    # fecha = models.DateField(default=datetime.now, blank=True, editable=True)
    email = models.EmailField(
        max_length=128,
        blank=True,
        null=True,
        default="---@gmail.com",
    )
    estado = models.CharField(
        max_length=20, choices=ESTADO_PEDIDO, default="A CONFIRMAR"
    )
    total = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    total_mas_envio = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    referencia = models.CharField(max_length=20, default="")
    
    tipo_transporte = models.CharField(
        max_length=15, blank=True, null=True, choices=TIPO_ENVIO, default="EN FABRICA"
    )
    condicion_afip = models.CharField(
        max_length=30, choices=AFIP, default="Consumidor Final", blank=True, null=True 
    )
    razon_social = models.CharField(
        max_length=128, blank=True, null=True, default="---"
    )
    domicilio_comercial = models.CharField(
        max_length=128, blank=True, null=True, default="---"
    )

    nombre_apellido_recibe = models.CharField( max_length=128,blank=True, null=True, default="---")
    documento_recibe = models.CharField( max_length=20,blank=True, null=True, default="---")
    domicilio_recibe = models.CharField(max_length=50, blank=True, null=True, default="---")
    localidad_recibe = models.CharField(max_length=50, blank=True, null=True, default="---")
    provincia_recibe = models.CharField(max_length=50, choices=PROVINCIA, default=BSAS)
    codigo_postal_recibe = models.CharField(max_length=8, blank=True, null=True, default="---")
    telefono_recibe = models.CharField(max_length=15, blank=True, null=True, default="---")

    envio_otro = models.BooleanField(default=False)


    class Meta:
        ordering = ("-created",)
        verbose_name = "Pedido"
        verbose_name_plural = "Pedido"

    def __str__(
        self,
    ):
        return f"Pedido {self.id}"

    def estado_de_pedido(self):
        if self.estado == "A CONFIRMAR":
            return format_html(
                '<span style="background-color:#EB6300; color: #fff; padding:7px;">{}</span>',
                self.estado,
            )
        if self.estado == "NO ACREDITADO":
            return format_html(
                '<span style="background-color:#F00; color: #fff; padding:7px;">{}</span>',
                self.estado,
            )
        if self.estado == "ACREDITADO":
            return format_html(
                '<span style="background-color:#0f0; color: #000; padding:7px;">{}</span>',
                self.estado,
            )
        if self.estado == "FACTURADO":
            return format_html(
                '<span style="background-color:#00f; color: #fff; padding:7px;">{}</span>',
                self.estado,
            )
        if self.estado == "DESPACHADO":
            return format_html(
                '<span style="background-color:#ccc; color: #444; padding:7px;">{}</span>',
                self.estado,
            )

    def get_total_price(self):
        total_cost = sum(item.get_total_price() for item in self.items.all())
        return total_cost

    def get_peso_total(self):
        peso_total = sum(item.get_peso_total() for item in self.items.all())
        return peso_total

    def get_description(self):
        return ", ".join(
            [f"{item.cantidad}x {item.cada_producto}" for item in self.items.all()]
        )


class Item(models.Model):

    pedido = models.ForeignKey(Pedido, related_name="items", on_delete=models.CASCADE)
    cada_producto = models.ForeignKey(Producto, related_name="pedido_items", on_delete=models.CASCADE) 
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=12, decimal_places=2)
    peso = models.DecimalField(
        "Peso en Kg", max_digits=12, decimal_places=3, default=0.000
    )
    descuento = models.DecimalField(max_digits=5, decimal_places=2, default=00.0)
    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Items"

    def __str__(self):
        return str(self.id)

    def get_total_price(self):
        return self.cantidad * (self.precio - (self.precio * self.descuento) / 100)

    def get_peso_total(self):
        return self.peso * self.cantidad


class EnviarFactura(models.Model):

    ENVIAR_FAC = [
        ("NO", "NO"),
        ("SI", "SI"),
    ]

    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    factura = models.FileField(upload_to="facturas/%Y/%m/%d", blank=True, null=True)
    mensaje = models.TextField(default="")
    enviar = models.CharField(max_length=5, choices=ENVIAR_FAC, default="NO")

    class Meta:
        verbose_name = "Enviar Factura"
        verbose_name_plural = "Enviar Factura"

    def create_mensaje(self):
        subject = "TIENDA-LIQUIDAMBAR.COM - FACTURA"
        from_email = "liquidambar.almacen.natural@gmail.com"
        destino = [self.pedido.email]
        mensaje_html = self.mensaje

        email = EmailMessage(
            subject,
            mensaje_html,
            from_email,
            destino,
            headers={'Reply-To': from_email}
        )

        # Verificar si existe un archivo adjunto
        if self.factura:
            try:
                # Abre el archivo en modo binario y adjúntalo
                with self.factura.open('rb') as uploaded_file:
                    email.attach(self.factura.name, uploaded_file.read(), 'application/pdf')
            except Exception as e:
                print(f"No se ha adjuntado archivo: {e}")

        email.send()

    def save(self, *args, **kwargs):
        # Guarda el archivo antes de enviar el mensaje
        super().save(*args, **kwargs)
        # Envía el correo después de que el archivo esté disponible
        if self.enviar == "SI":
            self.create_mensaje()