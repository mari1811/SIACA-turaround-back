from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import maquinaria, codigos_demora, turnaround, usuario, aerolinea, plantilla, vuelo, tarea, subtarea
import json

# Create your views here.

class MaquinariaView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request):
        maquinarias = list(maquinaria.objects.values())
        if len(maquinarias)>0:
            datos={'mensaje':'Success','maquinarias':maquinarias}
        else:
            datos={'mensaje':'No hay maquinarias'}
        return JsonResponse(datos)

    def post(self, request):
        jsondata = json.loads(request.body)
        maquinaria.objects.create(identificador=jsondata['identificador'], modelo=jsondata['modelo'], combustible=jsondata['combustible'], estado=jsondata['estado'], categoria=jsondata['categoria'] ,imagen=jsondata['imagen'])
        datos={'mensaje':'Success'}
        return JsonResponse(datos)

    def put(self, request, id):
        jsondata = json.loads(request.body)
        maquinarias = list(maquinaria.objects.filter(id=id).values())
        if len(maquinarias)>0:
            maquina = maquinaria.objects.get(id=id)
            maquina.identificador = jsondata['identificador']
            maquina.modelo = jsondata['modelo']
            maquina.combustible = jsondata['combustible']
            maquina.estado = jsondata['estado']
            maquina.categoria = jsondata['categoria']
            maquina.imagen = jsondata['imagen']
            maquina.save()
            datos={'mensaje':'Success'}
        else:
            datos={'mensaje':'No hay maquinarias'}
        return JsonResponse(datos)

    def delete(self, request, id):
        maquinarias = list(maquinaria.objects.filter(id=id).values())
        if len(maquinarias)>0:
            maquinaria.objects.filter(id=id).delete()
            datos={'mensaje':'Success'}
        else:
            datos={'mensaje':'No hay maquinarias'}
        return JsonResponse(datos)
    

class CodigoDemoraView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request):
        codigo = list(codigos_demora.objects.values())
        if len(codigo)>0:
            datos={'mensaje':'Success','codigoss':codigo}
        else:
            datos={'mensaje':'No hay codigos'}
        return JsonResponse(datos)
    

class TurnaroundView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request):
        turnarounds = list(turnaround.objects.values())
        if len(turnarounds)>0:
            datos={'mensaje':'Success','turnarounds':turnarounds}
        else:
            datos={'mensaje':'No hay turnarounds'}
        return JsonResponse(datos)
    
class UsuarioView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request):
        usuarios = list(usuario.objects.values())
        if len(usuarios)>0:
            datos={'mensaje':'Success','usuarios':usuarios}
        else:
            datos={'mensaje':'No hay usuarios'}
        return JsonResponse(datos)
    
    def post(self, request):
        jsondata = json.loads(request.body)
        usuario.objects.create(cedula=jsondata['cedula'], cargo=jsondata['cargo'], departameto=jsondata['departamento'], correo=jsondata['correo'], telefono=jsondata['telefono'], turno=jsondata['turno'] ,contrasena=jsondata['contrasena'], estado=jsondata['estado'] ,imagen=jsondata['imagen'])
        datos={'mensaje':'Success'}
        return JsonResponse(datos)
    
    def put(self, request, id):
        jsondata = json.loads(request.body)
        usuarios = list(usuario.objects.filter(id=id).values())
        if len(usuarios)>0:
            dato = usuario.objects.get(id=id)
            dato.cedula = jsondata['cedula']
            dato.cargo = jsondata['cargo']
            dato.departameto = jsondata['departamento']
            dato.correo = jsondata['correo']
            dato.telefono = jsondata['telefono']
            dato.turno = jsondata['turno']
            dato.contrasena = jsondata['contrasena']
            dato.estado = jsondata['estado']
            dato.imagen = jsondata['imagen']
            dato.save()
            datos={'mensaje':'Success'}
        else:
            datos={'mensaje':'No existe el usuario'}
        return JsonResponse(datos) 
    
    def delete(self, request, id):
        usuarios = list(usuario.objects.filter(id=id).values())
        if len(usuarios)>0:
            usuario.objects.filter(id=id).delete()
            datos={'mensaje':'Success'}
        else:
            datos={'mensaje':'No existe ese usuario'}
        return JsonResponse(datos)
    

class AerolineaView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request):
        aerolineas = list(aerolinea.objects.values())
        if len(aerolineas)>0:
            datos={'mensaje':'Success','aerolineas':aerolineas}
        else:
            datos={'mensaje':'No hay aerolineas'}
        return JsonResponse(datos)
    
    def post(self, request):
        jsondata = json.loads(request.body)
        aerolinea.objects.create(nombre=jsondata['nombre'], correo=jsondata['correo'], telefono=jsondata['telefono'], codigo=jsondata['codigo'], imagen=jsondata['imagen'])
        datos={'mensaje':'Success'}
        return JsonResponse(datos)
    
    def put(self, request, id):
        jsondata = json.loads(request.body)
        aerolineas = list(aerolinea.objects.filter(id=id).values())
        if len(aerolineas)>0:
            dato = aerolinea.objects.get(id=id)
            dato.nombre = jsondata['nombre']
            dato.correo = jsondata['correo']
            dato.telefono=jsondata['telefono']
            dato.codigo=jsondata['codigo']
            dato.imagen = jsondata['imagen']
            dato.save()
            datos={'mensaje':'Success'}
        else:
            datos={'mensaje':'No existe la aerolinea'}
        return JsonResponse(datos) 
    
    def delete(self, request, id):
        aerolineas = list(aerolinea.objects.filter(id=id).values())
        if len(aerolineas)>0:
            aerolinea.objects.filter(id=id).delete()
            datos={'mensaje':'Success'}
        else:
            datos={'mensaje':'No existe la aerolinea'}
        return JsonResponse(datos)

class PlantillaView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request):
        plantillas = list(plantilla.objects.values())
        if len(plantillas)>0:
            datos={'mensaje':'Success','plantillas':plantillas}
        else:
            datos={'mensaje':'No hay plantillas'}
        return JsonResponse(datos)
    
    def post(self, request):
        jsondata = json.loads(request.body)
        plantilla.objects.create(titulo=jsondata['titulo'])
        datos={'mensaje':'Success'}
        return JsonResponse(datos)
    
    def put(self, request, id):
        jsondata = json.loads(request.body)
        plantillas = list(plantilla.objects.filter(id=id).values())
        if len(plantillas)>0:
            dato = plantilla.objects.get(id=id)
            dato.titulo = jsondata['titulo']
            dato.save()
            datos={'mensaje':'Success'}
        else:
            datos={'mensaje':'No existe la plantilla'}
        return JsonResponse(datos) 
    
    def delete(self, request, id):
        plantillas = list(plantilla.objects.filter(id=id).values())
        if len(plantillas)>0:
            plantilla.objects.filter(id=id).delete()
            datos={'mensaje':'Success'}
        else:
            datos={'mensaje':'No existe la plantilla'}
        return JsonResponse(datos)
    

class TareaView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request):
        tareas = list(tarea.objects.values())
        if len(tareas)>0:
            datos={'mensaje':'Success','tareas':tareas}
        else:
            datos={'mensaje':'No hay tareas'}
        return JsonResponse(datos)
    
    def post(self, request):
        jsondata = json.loads(request.body)
        tarea.objects.create(titulo=jsondata['titulo'])
        datos={'mensaje':'Success'}
        return JsonResponse(datos)
    
    def put(self, request, id):
        jsondata = json.loads(request.body)
        tareas = list(tarea.objects.filter(id=id).values())
        if len(tareas)>0:
            dato = tarea.objects.get(id=id)
            dato.titulo = jsondata['titulo']
            dato.save()
            datos={'mensaje':'Success'}
        else:
            datos={'mensaje':'No existe la tarea'}
        return JsonResponse(datos)
    
    def delete(self, request, id):
        tareas = list(tarea.objects.filter(id=id).values())
        if len(tareas)>0:
            tarea.objects.filter(id=id).delete()
            datos={'mensaje':'Success'}
        else:
            datos={'mensaje':'No existe la tarea'}
        return JsonResponse(datos)
    

class SubtareaView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request):
        subtareas = list(subtarea.objects.values())
        if len(subtareas)>0:
            datos={'mensaje':'Success','subtareas':subtareas}
        else:
            datos={'mensaje':'No hay subtareas'}
        return JsonResponse(datos)
    
    def post(self, request):
        jsondata = json.loads(request.body)
        subtarea.objects.create(titulo=jsondata['titulo'], tipo=jsondata['tipo'], imagen=jsondata['imagen'], hora_inicio=jsondata['hora_inicio'], hora_fin=jsondata['hora_fin'], comentario=jsondata['comentario'])
        datos={'mensaje':'Success'}
        return JsonResponse(datos)
    
    def put(self, request, id):
        jsondata = json.loads(request.body)
        subtareas = list(subtarea.objects.filter(id=id).values())
        if len(subtareas)>0:
            dato = subtarea.objects.get(id=id)
            dato.titulo = jsondata['titulo']
            dato.tipo=jsondata['tipo']
            dato.imagen=jsondata['imagen']
            dato.hora_inicio=jsondata['hora_inicio']
            dato.hora_fin=jsondata['hora_fin']
            dato.comentario=jsondata['comentario']
            dato.save()
            datos={'mensaje':'Success'}
        else:
            datos={'mensaje':'No existe la subtarea'}
        return JsonResponse(datos)
    
    def delete(self, request, id):
        subtareas = list(subtarea.objects.filter(id=id).values())
        if len(subtareas)>0:
            subtarea.objects.filter(id=id).delete()
            datos={'mensaje':'Success'}
        else:
            datos={'mensaje':'No existe la subtarea'}
        return JsonResponse(datos)
    

class VueloView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request):
        vuelos = list(vuelo.objects.values())
        if len(vuelos)>0:
            datos={'mensaje':'Success','vuelos':vuelos}
        else:
            datos={'mensaje':'No hay vuelos'}
        return JsonResponse(datos)
    
    def post(self, request):
        jsondata = json.loads(request.body)
        vuelo.objects.create(ac_reg=jsondata['ac_reg'], ac_type=jsondata['ac_type'], estado=jsondata['estado'], lugar_salida=jsondata['lugar_salida'], lugar_destino=jsondata['lugar_destino'], fecha_llegada=jsondata['fecha_llegada'], hora_llegada=jsondata['hora_llegada'], ente_pagador=jsondata['ente_pagador'], numero_vuelo=jsondata['numero_vuelo'], ETA=jsondata['ETA'], ETD=jsondata['ETD'], ATA=jsondata['ATA'], ATD=jsondata['ATD'], gate=jsondata['gate'], tipo_vuelo=jsondata['tipo_vuelo'])
        datos={'mensaje':'Success'}
        return JsonResponse(datos)
    
    def put(self, request, id):
        jsondata = json.loads(request.body)
        vuelos = list(vuelo.objects.filter(id=id).values())
        if len(vuelos)>0:
            dato = vuelo.objects.get(id=id)
            dato.ac_reg =jsondata['ac_reg']
            dato.ac_type=jsondata['ac_type']
            dato.estado=jsondata['estado']
            dato.lugar_salida=jsondata['lugar_salida']
            dato.lugar_destino=jsondata['lugar_destino']
            dato.fecha_llegada= jsondata['fecha_llegada']
            dato.hora_llegada=jsondata['hora_llegada']
            dato.ente_pagador=jsondata['ente_pagador']
            dato.numero_vuelo=jsondata['numero_vuelo']
            dato.ETA=jsondata['ETA']
            dato.ETD=jsondata['ETD']
            dato.ATA=jsondata['ATA']
            dato.ATD=jsondata['ATD']
            dato.gate=jsondata['gate']
            dato.tipo_vuelo=jsondata['tipo_vuelo']
            dato.save()
            datos={'mensaje':'Success'}
        else:
            datos={'mensaje':'No existe el vuelo'}
        return JsonResponse(datos)
    
    def delete(self, request, id):
        vuelos = list(vuelo.objects.filter(id=id).values())
        if len(vuelos)>0:
            vuelo.objects.filter(id=id).delete()
            datos={'mensaje':'Success'}
        else:
            datos={'mensaje':'No existe el vuelo'}
        return JsonResponse(datos)