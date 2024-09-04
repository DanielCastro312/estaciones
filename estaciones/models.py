from django.db import models

class Estacion(models.Model):
    razon_social = models.CharField(max_length=255)
    url = models.URLField(max_length=255)
    direccion = models.CharField(max_length=255)
    puerto = models.IntegerField()
    usuario = models.CharField(max_length=100)
    clave = models.CharField(max_length=100)
    observacion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.razon_social
