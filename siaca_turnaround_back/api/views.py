from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import maquinaria
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