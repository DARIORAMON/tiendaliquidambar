from django.db import models

class ConfiguracionEnvio(models.Model):
    codigo_postal_base = models.CharField(max_length=10, help_text="Código postal de la dirección base")
    calle = models.CharField(max_length=255)
    altura = models.CharField(max_length=10)
    localidad = models.CharField(max_length=255)
    provincia = models.CharField(max_length=255)
    tarifa_por_km = models.DecimalField(max_digits=10, decimal_places=2, help_text="Costo por kilómetro")

    def __str__(self):
        return f"{self.codigo_postal_base} - {self.localidad}, {self.provincia}"