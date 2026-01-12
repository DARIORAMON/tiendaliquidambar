from django.db import models
from productos.models import Producto
from ckeditor_uploader.fields import RichTextUploadingField
from simple_history.models import HistoricalRecords

class CarrouselIntroduccion(models.Model):

    UNO = 1
    DOS = 2
    TRES = 3
    CUATRO = 4
    ORDEN = (
        (UNO, 1),
        (DOS, 2),
        (TRES, 3),
        (CUATRO, 4),
    )
    NADA = "---"
    NOVEDADES = "Novedades"
    OFERTAS = "Ofertas"
    VOLVIOAENTRAR = "Volvío a Entrar"
    DESTACADOS = "Destacados"

    LA_LINEA = (
        (NADA, "---"),
        (NOVEDADES, "Novedades"),
        (OFERTAS, "Ofertas"),
        (VOLVIOAENTRAR, "Volvío a Entrar"),
        (DESTACADOS, "Destacados"),
    )
    orden = models.IntegerField(choices=ORDEN, default=UNO)
    titulo = models.CharField(max_length=50, choices=LA_LINEA, default=NADA)
    imagen = models.ImageField(
        upload_to="carrouselle_intro/%Y/%m/%d", blank=True, null=True
    )
    descripcion = models.CharField(
        "Descripcion (220)", max_length=220, blank=True, null=True
    )
    ir_a = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        verbose_name = "Introducción Carrouselle"
        verbose_name_plural = "Introducción Carrouselle"


class ProductosDestacados(models.Model):
    UNO = 1
    DOS = 2
    TRES = 3

    ORDEN = (
        (UNO, 1),
        (DOS, 2),
        (TRES, 3),
    )

    orden = models.IntegerField(choices=ORDEN, default=UNO)
    producto = models.ForeignKey(
        Producto, blank=False, null=True, on_delete=models.CASCADE
    )
    imagen = models.ImageField(
        upload_to="productos_destacados_intro/%Y/%m/%d", blank=True, null=True
    )
    descripcion = models.CharField(
        "Descripcion (150)", max_length=150, blank=True, null=True
    )

    class Meta:
        verbose_name = "Introducción Productos Destacados"
        verbose_name_plural = "Introducción Productos Destacados"


class AireLibre(models.Model):
    imagen = models.ImageField(upload_to="aire_libre/%Y/%m/%d", blank=True, null=True)

    class Meta:
        verbose_name = "Introducción Aire Libre"
        verbose_name_plural = "Introducción Aire Libre"

    def __str__(
        self,
    ):
        return "Completar sección de Aire Libre"


class AireLibreBeneficios(models.Model):

    beneficio = models.ForeignKey(
        AireLibre, blank=False, null=True, on_delete=models.CASCADE
    )
    titulo = models.CharField("Título (40)", max_length=40, blank=True, null=True)
    descripcion = models.CharField(
        "Descripcion (220)", max_length=150, blank=True, null=True
    )


class Temporada(models.Model):
    imagen = models.ImageField(
        upload_to="intro_temporada/%Y/%m/%d", blank=True, null=True
    )
    iframe = models.CharField(max_length=600, blank=True, null=True)
    titulo = models.CharField("Título (40)", max_length=40, blank=True, null=True)
    subtitulo = models.CharField("Subtítulo (80)", max_length=80, blank=True, null=True)
    descripcion = models.CharField(
        "Descripcion (220)", max_length=220, blank=True, null=True
    )

    class Meta:
        verbose_name = "Introducción Temporada"
        verbose_name_plural = "Introducción Temporada"

 
class PreguntasFrecuentes(models.Model):

    pregunta = models.CharField(max_length=160, blank=True, null=True)
    descripcion = models.TextField( blank=True, null=True)
    contenido = RichTextUploadingField('contenido', blank=True, null=True)
    history = HistoricalRecords()
    
    class Meta:
        verbose_name = "Preguntas Frecuentes"
        verbose_name_plural = "Preguntas Frecuentes"

