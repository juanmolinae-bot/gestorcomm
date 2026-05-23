from django.contrib import admin
from .models import Zona, Incidencia


@admin.register(Zona)
class ZonaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')


@admin.register(Incidencia)
class IncidenciaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'zona', 'prioridad', 'estado', 'responsable', 'fecha_creacion')
    list_filter = ('estado', 'prioridad', 'zona')
    search_fields = ('titulo', 'descripcion')
