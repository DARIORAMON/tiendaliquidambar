from django.db import models
from .categoria import Categoria
from django.utils.html import format_html
from autoslug import AutoSlugField
from django.urls import reverse

class Producto(models.Model):

    Borrador = "Borrador"
    Publicado = "Publicado"
    Retirado = "Retirado"
    APROBACION_PRODUCTO = (
        (Borrador, "Borrador"),
        (Publicado, "Publicado"),
        (Retirado, "Retirado"),
    )

    articulo = models.CharField(max_length=50)
    name = models.CharField(max_length=50, verbose_name="Nombre")
    composicion = models.CharField(max_length=200)
    slug = AutoSlugField(unique=True, always_update=True, populate_from="name")
    descripcion = models.CharField(max_length=200, default="")
    imagen = models.ImageField(upload_to="producto/%Y/%m/%d", blank=True, null=True)
    categoria = models.ManyToManyField(Categoria, verbose_name="Línea")
    precio = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    descuento = models.IntegerField(default=0)
    precio_mayorista = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    descuento_mayorista = models.IntegerField(default=0)
    estado = models.CharField(
        max_length=10, choices=APROBACION_PRODUCTO, default="Borrador"
    )
    peso = models.DecimalField("Peso en Kg", max_digits=12, decimal_places=3, default=0.000)
    stock=models.IntegerField(default=0)

    es_oferta = models.BooleanField(default=False, verbose_name="¿Es Oferta?")
    precio_oferta = models.FloatField(blank=True, null=True, verbose_name="Precio de Oferta")


    @staticmethod
    def get_productos_by_id(ids):
        return Producto.objects.filter(id__in=ids)

    @staticmethod
    def get_all_productos():
        return Producto.objects.all()

    @staticmethod
    def get_all_productos_by_categoria_id(categoria_id):
        if categoria_id:
            return Producto.objects.filter(categoria=categoria_id)
        else:
            return Producto.objects.all()

    def estado_de_producto(self):
        if self.estado == "Retirado":
            return format_html(
                '<span style="color: #f00;">{}</span>',
                self.estado,
            )
        elif self.estado == "Borrador":
            return format_html(
                '<span style="color: #f0f;">{}</span>',
                self.estado,
            )
        elif self.estado == "Publicado":
            return format_html(
                '<span style="color: #099;">{}</span>',
                self.estado,
            )


    def categorias_del_producto(self):

        cat = self.categoria.all()
        cate = ""
        for cat in cat:
            cate = cate + " - " + cat.nombre
        return cate

    def __str__(self,):
        return self.articulo


    def get_absolute_url(self):
        return f"/tienda/ver_producto/{self.articulo}/"


class ImagenProducto(models.Model):
    producto = models.ForeignKey(
        Producto, blank=False, null=True, on_delete=models.CASCADE
    )
    nombre = models.CharField(max_length=128)
    imagen = models.FileField(
        upload_to="imagen_producto/%Y/%m/%d",
        default="defecto/defecto.png",
        blank=False,
        null=False,
    )

    def __str__(self):
        return "%s" % self.nombre

