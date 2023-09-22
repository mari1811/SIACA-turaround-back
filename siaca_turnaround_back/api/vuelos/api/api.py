from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .serializer import VueloSerializer, ListaVuelosSerializer, CiudadesSerializer, TipoVueloSerializer, TipoServicioSerializer, REGSerializer
from api.models import vuelo, ciudades, tipo_vuelo, tipo_servicio
from rest_framework import filters
from rest_framework import generics
from rest_framework.authtoken.models import Token



class Vuelo(APIView):

    #Lista de Vuelos
    def get(self, request, *args, **kwargs):
        
            token = request.GET.get('token')
            token = Token.objects.filter(key = token).first()
            if token:
                vuelos = vuelo.objects.all()
                vuelos_serializer = VueloSerializer(vuelos, many = True)
                return Response (vuelos_serializer.data, status=status.HTTP_200_OK)

            return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)
    #Crear un Vuelo      
    def post(self, request, *args, **kwargs):
        
            token = request.GET.get('token')
            token = Token.objects.filter(key = token).first()
            if token:
                vuelos_serializer = VueloSerializer(data = request.data)
                if vuelos_serializer.is_valid():
                    vuelos_serializer.save()
                    return Response(vuelos_serializer.data, status=status.HTTP_201_CREATED)
                
            return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)

class ModificarVuelo(generics.RetrieveUpdateDestroyAPIView):
    
    #Buscar un vuelo específico
    def get(self, request, pk=None, *args, **kwargs):
        token = request.GET.get('token')
        token = Token.objects.filter(key = token).first()
        if token:
            fly = vuelo.objects.filter(id = pk).first()
            if fly:
                vuelo_serializer = ListaVuelosSerializer(fly)
                return Response(vuelo_serializer.data, status=status.HTTP_200_OK)
            return Response({'mensaje':'No se ha encontrado el vuelo'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)
    
    #Editar un vuelo
    def patch(self, request, pk=None, *args, **kwargs):
        token = request.GET.get('token')
        token = Token.objects.filter(key = token).first()
        if token:
            fly = vuelo.objects.filter(id = pk).first()
            if fly:
                vuelo_serializer = VueloSerializer(fly, data=request.data)
                if vuelo_serializer.is_valid():
                    vuelo_serializer.save()
                    return Response(vuelo_serializer.data, status=status.HTTP_200_OK)
            return Response({'mensaje':'No se ha encontrado el vuelo'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)
        
    #Eliminar un vuelo
    def delete(self, request, pk=None, *args, **kwargs):
        token = request.GET.get('token')
        token = Token.objects.filter(key = token).first()
        if token:
            fly = vuelo.objects.filter(id = pk).first()
            if fly:
                fly.delete()
                return Response({'mensaje':'Vuelo eliminado'}, status=status.HTTP_200_OK)
            return Response({'mensaje':'No se ha encontrado el vuelo'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)
    
    
class VueloDetalle(APIView):

    #Lista de Vuelos
    def get(self, request, *args, **kwargs):
        
            token = request.GET.get('token')
            token = Token.objects.filter(key = token).first()
            if token:
                vuelos = vuelo.objects.all()
                vuelos_serializer = ListaVuelosSerializer(vuelos, many = True)
                return Response (vuelos_serializer.data, status=status.HTTP_200_OK)

            return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)
    


class BuscarVueloFecha(APIView):
        
        def get(self, request, fecha=None, *args, **kwargs):
            token = request.GET.get('token')
            token = Token.objects.filter(key = token).first()
            if token:
                fly = vuelo.objects.filter(ETA_fecha = fecha)
                if fly:
                    vuelo_serializer = ListaVuelosSerializer(fly, many = True)
                    return Response(vuelo_serializer.data, status=status.HTTP_200_OK)
                return Response({'mensaje':'No hay vuelos en esa fecha'}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)
        
class Ciudades(APIView):

    #Lista de Ciudades
    def get(self, request, *args, **kwargs):
        
            token = request.GET.get('token')
            token = Token.objects.filter(key = token).first()
            if token:
                ciudad = ciudades.objects.all()
                ciudades_serializer = CiudadesSerializer(ciudad, many = True)
                return Response (ciudades_serializer.data, status=status.HTTP_200_OK)
            

class TipoVuelo(APIView):

    #Lista tipo de vuelo
    def get(self, request, *args, **kwargs):
        
            token = request.GET.get('token')
            token = Token.objects.filter(key = token).first()
            if token:
                tipo = tipo_vuelo.objects.all()
                tipo_serializer = TipoVueloSerializer(tipo, many = True)
                return Response (tipo_serializer.data, status=status.HTTP_200_OK)


class TipoServicio(APIView):

    #Lista tipo de vuelo
    def get(self, request, *args, **kwargs):
        
            token = request.GET.get('token')
            token = Token.objects.filter(key = token).first()
            if token:
                tipo = tipo_servicio.objects.all()
                tipo_serializer = TipoServicioSerializer(tipo, many = True)
                return Response (tipo_serializer.data, status=status.HTTP_200_OK)


class ModificarCiudades(generics.RetrieveUpdateDestroyAPIView):

  #Buscar un ciudad específico
    def get(self, request, pk=None, *args, **kwargs):
        token = request.GET.get('token')
        token = Token.objects.filter(key = token).first()
        if token:
            ciudad = ciudades.objects.filter(id = pk).first()
            if ciudad:
                ciudad_serializer = CiudadesSerializer(ciudad)
                return Response(ciudad_serializer.data, status=status.HTTP_200_OK)
            return Response({'mensaje':'No se ha encontrado el vuelo'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)
    
    #Agergar ciudad
    def post(self, request, *args, **kwargs):
        
            token = request.GET.get('token')
            token = Token.objects.filter(key = token).first()
            if token:
                ciudades_serializer = CiudadesSerializer(data = request.data)
                if ciudades_serializer.is_valid():
                    ciudades_serializer.save()
                    return Response(ciudades_serializer.data, status=status.HTTP_201_CREATED)
                
            return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)
    
    #Editar una ciudad
    def patch(self, request, pk=None, *args, **kwargs):
        token = request.GET.get('token')
        token = Token.objects.filter(key = token).first()
        if token:
            ciudad = ciudades.objects.filter(id = pk).first()
            if ciudad:
                ciuaddes_serializer = CiudadesSerializer(ciudad, data=request.data)
                if ciuaddes_serializer.is_valid():
                    ciuaddes_serializer.save()
                    return Response(ciuaddes_serializer.data, status=status.HTTP_200_OK)
            return Response({'mensaje':'No se ha encontrado la ciudad'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)
        
    #Eliminar una ciudad
    def delete(self, request, pk=None, *args, **kwargs):
        token = request.GET.get('token')
        token = Token.objects.filter(key = token).first()
        if token:
            ciudad = ciudades.objects.filter(id = pk).first()
            if ciudad:
                ciudad.delete()
                return Response({'mensaje':'Ciudad eliminada'}, status=status.HTTP_200_OK)
            return Response({'mensaje':'No se ha encontrado la ciudad'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)


class REG(APIView):

    #Filtro de REG
    def get(self, request, *args, **kwargs):
        
            token = request.GET.get('token')
            token = Token.objects.filter(key = token).first()
            if token:
                reg = vuelo.objects.order_by("ac_reg").values("ac_reg", "fk_aerolinea_id").distinct()
                reg_serializer = REGSerializer(reg, many = True)
                return Response (reg_serializer.data, status=status.HTTP_200_OK)
            
            return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)



class BuscarVueloAerolinea(APIView):
        
        def get(self, request, pk=None, *args, **kwargs):
            token = request.GET.get('token')
            token = Token.objects.filter(key = token).first()
            if token:
                fly = vuelo.objects.filter(fk_aerolinea_id = pk).order_by("-ETD_fecha")
                if fly:
                    vuelo_serializer = ListaVuelosSerializer(fly, many = True)
                    return Response(vuelo_serializer.data, status=status.HTTP_200_OK)
                return Response({'mensaje':'No hay vuelos en esta aerolinea'}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)