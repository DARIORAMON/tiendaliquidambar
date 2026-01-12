from django.db import models

class Categoria(models.Model):
    
    NADA="---"
    FRUTAS_SECAS="Frutas secas"
    MIX="Mix"
    GRANOLAS="Granolas"
    ALMOHADITAS="Almohaditas"
    SEMILLAS="Semillas"
    HARINAS="Harinas"
    SUPLEMENTOS_NATURALES="Suplementos naturales"
    ACEITES ="Aceites"
    PANIFICADOS ="Panificados"
    GALLETAS ="Galletas"
    ALFAJORES ="Alfajores"
    PRODUCTOS_SIN_GLUTEN ="Productos sin gluten"
    CONGELADOS ="Congelados"
    PRODUCTOS_VEGANOS ="Productos veganos"
    PRODUCTOS_SIN_AZUCAR ="Productos sin azucar"
    HIERBAS ="Hierbas"
    DEPORTES ="Deportes"
    INFUSIONES ="Infusiones"


 

    LA_LINEA = (
        (NADA, "---"),
        (FRUTAS_SECAS, "Frutas secas"),
        (MIX, "Mix"),
        (GRANOLAS, "Granolas"),
        (ALMOHADITAS, "Almohaditas"),
        (SEMILLAS, "Semillas"),
        (HARINAS, "Harinas"),
        (SUPLEMENTOS_NATURALES, "Suplementos naturales"),
        (ACEITES, "Aceites"),
        (PANIFICADOS, "Panificados"),
        (GALLETAS, "Galletas"),
        (ALFAJORES, "Alfajores"),
        (PRODUCTOS_SIN_GLUTEN, "Productos sin gluten"),
        (CONGELADOS, "Congelados"),
        (PRODUCTOS_VEGANOS, "Productos veganos"),
        (PRODUCTOS_SIN_AZUCAR, "Productos sin azucar"),
        (HIERBAS, "Hierbas"),
        (DEPORTES, "Deportes"),
        (INFUSIONES, "Infusiones"),
    )

    NADA="---"
    FRUTAS_SECAS="Frutas secas"
    MIX="Mix"
    GRANOLAS="Granolas"
    ALMOHADITAS="Almohaditas"
    SEMILLAS="Semillas"
    HARINAS="Harinas"
    SUPLEMENTOS_NATURALES="Suplementos naturales"
    ACEITES ="Aceites"
    PANIFICADOS ="Panificados"
    GALLETAS ="Galletas"
    ALFAJORES ="Alfajores"
    PRODUCTOS_SIN_GLUTEN ="Productos sin gluten"
    CONGELADOS ="Congelados"
    PRODUCTOS_VEGANOS ="Productos veganos"
    PRODUCTOS_SIN_AZUCAR ="Productos sin azucar"
    HIERBAS ="Hierbas"
    DEPORTES ="Deportes"
    INFUSIONES ="Infusiones"

    LA_LINEA_SLUG = (
        (NADA, "---"),
        (FRUTAS_SECAS, "Frutas secas"),
        (MIX, "Mix"),
        (GRANOLAS, "Granolas"),
        (ALMOHADITAS, "Almohaditas"),
        (SEMILLAS, "Semillas"),
        (HARINAS, "Harinas"),
        (SUPLEMENTOS_NATURALES, "Suplementos naturales"),
        (ACEITES, "Aceites"),
        (PANIFICADOS, "Panificados"),
        (GALLETAS, "Galletas"),
        (ALFAJORES, "Alfajores"),
        (PRODUCTOS_SIN_GLUTEN, "Productos sin gluten"),
        (CONGELADOS, "Congelados"),
        (PRODUCTOS_VEGANOS, "Productos veganos"),
        (PRODUCTOS_SIN_AZUCAR, "Productos sin azucar"),
        (HIERBAS, "Hierbas"),
        (DEPORTES, "Deportes"),
        (INFUSIONES, "Infusiones"),
    )

    UNO = 1
    DOS = 2
    TRES = 3
    CUATRO = 4
    CINCO = 5
    SEIS = 6
    SIETE = 7
    OCHO = 8
    NUEVE = 9
    DIEZ = 10
    ONCE = 11
    DOCE = 12
    TRECE = 13
    CATORCE = 14
    QUINCE = 15
    DIESISEIS = 16
    DIESISIETE = 17
    DIESIOCHO = 18
    DIESINUEVE = 19
    VEINTE = 20
    VEINTIUNO = 21
    VEINTIDOS = 22
    VEINTITRES = 23
    VEINTICUATRO = 24
    VEINTICINCO = 25
    VEINTISEIS = 26
    VEINTISIETE = 27
    VEINTIOCHO = 28
    VEINTINUEVE = 29
    TREINTA = 30
    TREINTAYUNO = 31
    TREINTAYDOS = 32
    TREINTAYTRES = 33
    TREINTAYCUATRO = 34
    TREINTAYCINCO = 35
    TREINTAYSEIS = 36
    TREINTAYSIETE = 37
    TREINTAYOCHO = 38
    TREINTAYNUEVE = 39
    CUARENTA = 40
    CURENTAYUNO = 41
    CUARENTAYDOS = 42
    CUARENTAYTRES = 43
    CUARENTAYCUATRO = 44
    CUARENTAYCINCO = 45
    CUARENTEYSEIS = 46
    CUARENTAYSIETE = 47
    CUARENTAYOCHO = 48
    CUARENTAYNUEVE = 49
    CINCUENTA = 50

    POSICION = (
        (UNO, 1),
        (DOS, 2),
        (TRES, 3),
        (CUATRO, 4),
        (CINCO, 5),
        (SEIS, 6),
        (SIETE, 7),
        (OCHO, 8),
        (NUEVE, 9),
        (DIEZ, 10),
        (ONCE, 11),
        (DOCE, 12),
        (TRECE, 13),
        (CATORCE, 14),
        (QUINCE, 15),
        (DIESISEIS, 16),
        (DIESISIETE, 17),
        (DIESIOCHO, 18),
        (DIESINUEVE, 19),
        (VEINTE, 20),
        (VEINTIUNO, 21),
        (VEINTIDOS, 22),
        (VEINTITRES, 23),
        (VEINTICUATRO, 24),
        (VEINTICINCO, 25),
        (VEINTISEIS, 26),
        (VEINTISIETE, 27),
        (VEINTIOCHO, 28),
        (VEINTINUEVE, 29),
        (TREINTA, 30),
        (TREINTAYUNO, 31),
        (TREINTAYDOS, 32),
        (TREINTAYTRES, 33),
        (TREINTAYCUATRO, 34),
        (TREINTAYCINCO, 35),
        (TREINTAYSEIS, 36),
        (TREINTAYSIETE, 37),
        (TREINTAYOCHO, 38),
        (TREINTAYNUEVE, 39),
        (CUARENTA, 40),
        (CURENTAYUNO, 41),
        (CUARENTAYDOS, 42),
        (CUARENTAYTRES, 43),
        (CUARENTAYCUATRO, 44),
        (CUARENTAYCINCO, 45),
        (CUARENTEYSEIS, 46),
        (CUARENTAYSIETE, 47),
        (CUARENTAYOCHO, 48),
        (CUARENTAYNUEVE, 49),
        (CINCUENTA, 50),
    )

    nombre = models.CharField(max_length=50, choices=LA_LINEA, default=NADA)
    slug = models.CharField(max_length=50, choices=LA_LINEA_SLUG, default=NADA)
    imagen = models.ImageField(upload_to="linea/%Y/%m/%d", blank=True, null=True)
    orden = models.IntegerField(choices=POSICION, default=UNO)

    class Meta:
        verbose_name = "CATEGORÍA"
        verbose_name_plural = "CATEGORÍA"
        ordering = ["orden"]

    def __str__(
        self,
    ):
        return self.nombre

    @staticmethod
    def get_all_categorias():
        return Categoria.objects.all()