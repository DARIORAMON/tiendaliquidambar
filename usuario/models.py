from django.db import models
from django.contrib.auth.models import User
User._meta.get_field("email")._unique = True

class Perfil(models.Model):

    A = "A"
    B = "B"
    C = "C"
    E = "E"
    
    FAC = (
        (A, "A"),
        (B, "B"),
        (C, "C"),
        (E, "E"),
    )

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


    PROVINCIA = [
        ("Buenos Aires", "Buenos Aires"),
        ("Capital Federal", "Capital Federal"),
        ("Catamarca", "Catamarca"),
        ("Chaco", "Chaco"),
        ("Chubut", "Chubut"),
        ("Córdoba", "Córdoba"),
        ("Corrientes", "Corrientes"),
        ("Entre Ríos", "Entre Ríos"),
        ("Formosa", "Formosa"),
        ("Jujuy", "Jujuy"),
        ("La Pampa", "La Pampa"),
        ("La Rioja", "La Rioja"),
        ("Mendoza", "Mendoza"),
        ("Misiones", "Misiones"),
        ("Neuquén", "Neuquén"),
        ("Río Negro", "Río Negro"),
        ("Salta", "Salta"),
        ("San Juan", "San Juan"),
        ("San Luis", "San Luis"),
        ("Santa Cruz", "Santa Cruz"),
        ("Santa Fe", "Santa Fe"),
        ("Santiago del Estero", "Santiago del Estero"),
        ("Tierra del Fuego", "Tierra del Fuego"),
        ("Tucumán", "Tucumán"),
    ]

    usuario = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )
    nombre = models.CharField(
        max_length=50,
    )
    apellido = models.CharField(
        max_length=50,
    )
    clave = models.CharField(max_length=50, blank=True, null=True, default="---")
    domicilio = models.CharField(
        max_length=50,
    )
    localidad = models.CharField(
        max_length=50,
    )
    provincia = models.CharField(max_length=50, choices=PROVINCIA)
    codigo_postal = models.CharField(
        max_length=8,
    )
    telefono_fijo = models.CharField(max_length=15, blank=True, null=True)
    celular = models.CharField(
        max_length=15,
    )
    cuil_cuit = models.CharField(
        max_length=20,
    )
    documento = models.CharField(
        max_length=20, blank=True, null=True)


    condicion_afip = models.CharField(
        max_length=30, choices=AFIP, blank=True, null=True 
    )
    razon_social = models.CharField(
        max_length=128, blank=True, null=True, default="---"
    )
    domicilio_comercial = models.CharField(
        max_length=128, blank=True, null=True, default="---"
    )



