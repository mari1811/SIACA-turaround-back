from django.contrib import admin
from .models import maquinaria,codigos_demora,turnaround,usuario,usuario_turnaround,aerolinea,plantilla,tarea,subtarea,vuelo,documento, cantidad_categoria, cargo, categoria, ciudades
from .models import Comentario, departamento, Hora, HoraInicioFin, Imagen, maquinaria_historial, tipo, tipo_servicio, tipo_subtarea, tipo_vuelo


# Register your models here.

admin.site.register(maquinaria)
admin.site.register(codigos_demora)
admin.site.register(turnaround)
admin.site.register(usuario)
admin.site.register(usuario_turnaround)
admin.site.register(aerolinea)
admin.site.register(plantilla)
admin.site.register(tarea)
admin.site.register(subtarea)
admin.site.register(vuelo)
admin.site.register(documento)
admin.site.register(cantidad_categoria)
admin.site.register(cargo)
admin.site.register(categoria)
admin.site.register(ciudades)
admin.site.register(Comentario)
admin.site.register(departamento)
admin.site.register(Hora)
admin.site.register(HoraInicioFin)
admin.site.register(Imagen)
admin.site.register(maquinaria_historial)
admin.site.register(tipo)
admin.site.register(tipo_vuelo)
admin.site.register(tipo_servicio)
admin.site.register(tipo_subtarea)
