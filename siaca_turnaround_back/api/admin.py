from django.contrib import admin
from .models import maquinaria,codigos_demora,turnaround,maquinaria_turnaround,usuario,usuario_turnaround,aerolinea,plantilla,tarea,subtarea,vuelo,documento


# Register your models here.

admin.site.register(maquinaria)
admin.site.register(codigos_demora)
admin.site.register(turnaround)
admin.site.register(maquinaria_turnaround)
admin.site.register(usuario)
admin.site.register(usuario_turnaround)
admin.site.register(aerolinea)
admin.site.register(plantilla)
admin.site.register(tarea)
admin.site.register(subtarea)
admin.site.register(vuelo)
admin.site.register(documento)