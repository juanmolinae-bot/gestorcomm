from django.db import models
from django.contrib.auth.models import User


class Zona(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)

    class Meta:
        verbose_name = "Zona"
        verbose_name_plural = "Zonas"

    def __str__(self):
        return self.nombre


class Incidencia(models.Model):
    ESTADOS = (
        ('abierta', 'Abierta'),
        ('en_revision', 'En revisión'),
        ('resuelta', 'Resuelta'),
        ('cerrada', 'Cerrada'),
    )

    PRIORIDADES = (
        ('baja', 'Baja'),
        ('media', 'Media'),
        ('alta', 'Alta'),
        ('critica', 'Crítica'),
    )

    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    zona = models.ForeignKey(Zona, on_delete=models.PROTECT, related_name='incidencias')
    prioridad = models.CharField(max_length=20, choices=PRIORIDADES, default='media')
    estado = models.CharField(max_length=20, choices=ESTADOS, default='abierta')
    responsable = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='incidencias')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Incidencia"
        verbose_name_plural = "Incidencias"
        ordering = ['-fecha_creacion']

    def __str__(self):
        return self.titulo
