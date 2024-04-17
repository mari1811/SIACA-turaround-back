from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .serializer import DocumentosDatosSerializer, VueloSerializer, DocumentosSerializer, HoraInicioSerializer, HoraInicioFinSerializer, ImagenSerializer, ComentarioSerializer, TurnaoundSerializer, CodigoSerializer
from api.models import documento, vuelo, maquinaria, Hora, HoraInicioFin, Comentario, Imagen, turnaround, codigos_demora
from api.models import turnaround, subtarea, Imagen, Hora, HoraInicioFin, Comentario
from rest_framework import filters
from rest_framework import generics
from rest_framework.authtoken.models import Token
import json
from django.http import JsonResponse
from django.core.serializers import serialize
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

from django.db.models import Q
from django.template.loader import render_to_string

class Documento(APIView):

    #Lista de Docuemntos
    def get(self, request, *args, **kwargs):
        
            token = request.GET.get('token')
            token = Token.objects.filter(key = token).first()
            if token:
                documentos = documento.objects.all()
                documento_serializer = DocumentosDatosSerializer(documentos, many = True)
                return Response (documento_serializer.data, status=status.HTTP_200_OK)

            return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)

    #Crear un Documento      
    def post(self, request, *args, **kwargs):
        
            token = request.GET.get('token')
            token = Token.objects.filter(key = token).first()
            if token:
                documento_serializer = DocumentosSerializer(data = request.data)
                if documento_serializer.is_valid():
                    documento_serializer.save()
                    return Response(documento_serializer.data, status=status.HTTP_201_CREATED)
                else:
                     return Response({'mensaje':'Data no válida'}, status=status.HTTP_400_BAD_REQUEST)
                
            return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)
    

class ComentarioTurnaround(APIView):

        #Agregar comentario a una subtarea del turaround
        def post(self, request, *args, **kwargs):
        
            token = request.GET.get('token')
            token = Token.objects.filter(key = token).first()
            if token:
                turnarounds_serializer = ComentarioSerializer(data = request.data)
                if turnarounds_serializer.is_valid():
                    turnarounds_serializer.save()
                    return Response(turnarounds_serializer.data, status=status.HTTP_201_CREATED)
                else:
                     return Response({'mensaje':'Data no válida'}, status=status.HTTP_400_BAD_REQUEST)
                
            return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)


class HoraInicioTurnaround(APIView):

        #Agregar hora de inicio a una subtarea del turnaround
        def post(self, request, *args, **kwargs):
        
            token = request.GET.get('token')
            token = Token.objects.filter(key = token).first()
            if token:
                turnarounds_serializer = HoraInicioSerializer(data = request.data)
                if turnarounds_serializer.is_valid():
                    turnarounds_serializer.save()
                    return Response(turnarounds_serializer.data, status=status.HTTP_201_CREATED)
                else:
                     return Response({'mensaje':'Data no válida'}, status=status.HTTP_400_BAD_REQUEST)
                
            return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)
        

class HoraInicioFinTurnaround(APIView):

        #Agregar hora de inicio y fin a una subtarea del turnaround 
        def post(self, request, *args, **kwargs):
        
            token = request.GET.get('token')
            token = Token.objects.filter(key = token).first()
            if token:
                turnarounds_serializer = HoraInicioFinSerializer(data = request.data)
                if turnarounds_serializer.is_valid():
                    turnarounds_serializer.save()
                    return Response(turnarounds_serializer.data, status=status.HTTP_201_CREATED)
                else:
                     return Response({'mensaje':'Data no válida'}, status=status.HTTP_400_BAD_REQUEST)
                
            return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)
        
class ImagenTurnaround(APIView):

        #Agregar hora una imagen a una subtarea del turnaround      
        def post(self, request, *args, **kwargs):
        
            token = request.GET.get('token')
            token = Token.objects.filter(key = token).first()
            if token:
                turnarounds_serializer = ImagenSerializer(data = request.data)
                if turnarounds_serializer.is_valid():
                    turnarounds_serializer.save()
                    return Response(turnarounds_serializer.data, status=status.HTTP_201_CREATED)
                else:
                     return Response({'mensaje':'Data no válida'}, status=status.HTTP_400_BAD_REQUEST)
                
            return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)
        

class TareasTurnaround(APIView):

    #Turnaround por ID con la infomación del vuelo y la plantilla asociada
    def get(self, request, pk=None, *args, **kwargs):
        
            token = request.GET.get('token')
            token = Token.objects.filter(key = token).first()
            if token:
                datos = turnaround.objects.filter(id = pk).first()
                documento_serializer = TurnaoundSerializer(datos)
                return Response (documento_serializer.data, status=status.HTTP_200_OK)

            return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)
    

class Turnarounds(APIView):

    #Turnaround por ID con la infomación del vuelo y la plantilla asociada
    def get(self, request, pk=None, *args, **kwargs):
        
            token = request.GET.get('token')
            token = Token.objects.filter(key = token).first()
            if token:
                imagenes = list(Imagen.objects.filter(fk_turnaround_id=pk).values('id','fk_subtarea__id','fk_subtarea__titulo', 'imagen','fk_subtarea__fk_tipo__nombre','fk_subtarea__fk_tarea__titulo'))
                horas = list(Hora.objects.filter(fk_turnaround_id=pk).values('id','fk_subtarea__id','fk_subtarea__titulo', 'hora_inicio','fk_subtarea__fk_tipo__nombre','fk_subtarea__fk_tarea__titulo'))
                horas_inicio_fin = list(HoraInicioFin.objects.filter(fk_turnaround_id=pk).values('id','fk_subtarea__id','fk_subtarea__titulo', 'hora_inicio', 'hora_fin','fk_subtarea__fk_tipo__nombre','fk_subtarea__fk_tarea__titulo'))
                comentarios = list(Comentario.objects.filter(fk_turnaround_id=pk).values('id','fk_subtarea__id','fk_subtarea__titulo', 'comentario','fk_subtarea__fk_tipo__nombre','fk_subtarea__fk_tarea__titulo'))


                return Response({
                'horas': horas,
                'horas_inicio_fin': horas_inicio_fin,
                'imagenes': imagenes,
                'comentarios': comentarios
            })

class TurnaroundCorreo(APIView):
    # Turnaround por ID con la información del vuelo y la plantilla asociada
    def get(self, request, pk=None, *args, **kwargs):
        token = request.GET.get('token')
        token = Token.objects.filter(key=token).first()
        if token:
            # Query the data as before
            horas = list(Hora.objects.filter(fk_turnaround_id=pk).values('fk_subtarea__titulo', 'hora_inicio'))
            horas_inicio_fin = list(HoraInicioFin.objects.filter(fk_turnaround_id=pk).values('fk_subtarea__titulo', 'hora_inicio', 'hora_fin'))
            comentarios = list(Comentario.objects.filter(fk_turnaround_id=pk).values('fk_subtarea__titulo', 'comentario'))
            datos = turnaround.objects.filter(id = pk).first()
            documento_serializer = TurnaoundSerializer(datos)


            if datos:
                # Format the data as specified
                formatted_data = ""
                formatted_data = "<table style='width:100%; border: 1px solid black; border-collapse: collapse;'>\n"
                formatted_data += "  <tr style='border: 1px solid black;'><th style='border: 1px solid black; padding: 5px;'>Task</th><th style='border: 1px solid black; padding: 5px;'>Time or Comment</th></tr>\n"

                for hora in horas:
                    formatted_data += f"  <tr style='border: 1px solid black;'><td style='border: 1px solid black; padding: 5px;'>{hora['fk_subtarea__titulo']}</td><td style='border: 1px solid black; padding: 5px;'>{hora['hora_inicio']}</td></tr>\n"

                for hora_inicio_fin in horas_inicio_fin:
                    formatted_data += f"  <tr style='border: 1px solid black;'><td style='border: 1px solid black; padding: 5px;'>{hora_inicio_fin['fk_subtarea__titulo']}</td><td style='border: 1px solid black; padding: 5px;'>{hora_inicio_fin['hora_inicio']} - {hora_inicio_fin['hora_fin']}</td></tr>\n"

                for comentario in comentarios:
                    formatted_data += f"  <tr style='border: 1px solid black;'><td style='border: 1px solid black; padding: 5px;'>{comentario['fk_subtarea__titulo']}</td><td style='border: 1px solid black; padding: 5px;'>{comentario['comentario']}</td></tr>\n"

                formatted_data += "</table>\n"

                # Send the email with the formatted data
                subject = 'Turnaround Information'
                message = f'<html><body>\n' 
                message+= f'<p>Los servicios de asistencia en tierra realizados por Siaca han sido completados exitosamente, el sistema generó el siguiente reporte: </p>\n'
                message+= f'<p>Datos del vuelo: </p>\n'
                message += f'<table style="width:100%; border: 0.5px solid black; border-collapse: collapse; border-radius: 5px;">\n'

                message += f'  <tr style="border: 0.5px solid black;"><th style="border: 0.5px solid black; padding: 5px;">Codigo de Demora:</th><td style="border: 0.5px solid black; padding: 5px;"><strong>Identificador:</strong> {documento_serializer.data["fk_codigos_demora"]["identificador"]} - <strong>Alpha:</strong> {documento_serializer.data["fk_codigos_demora"]["alpha"]}</td><td style="border: 0.5px solid black; padding: 5px;"><strong>Descripción:</strong> {documento_serializer.data["fk_codigos_demora"]["descripcion"]}</td><td style="border: 0.5px solid black; padding: 5px;"><strong>Accountable:</strong> {documento_serializer.data["fk_codigos_demora"]["accountable"]}</td></tr>\n'

                message += f'  <tr style="border: 0.5px solid black;"><th style="border: 0.5px solid black; padding: 5px;">Date and Start Time:</th><td style="border: 0.5px solid black; padding: 5px;">{documento_serializer.data["fecha_inicio"]} - {documento_serializer.data["hora_inicio"]}</td><th style="border: 0.5px solid black; padding: 5px;">Service Type:</th><td style="border: 0.5px solid black; padding: 5px;">{documento_serializer.data["fk_vuelo"]["tipo_servicio"]["nombre"]}</td></tr>\n'

                message += f'  <tr style="border: 0.5px solid black;"><th style="border: 0.5px solid black; padding: 5px;">STN:</th><td style="border: 0.5px solid black; padding: 5px;">{documento_serializer.data["fk_vuelo"]["stn_id"]["codigo"]}</td><th style="border: 0.5px solid black; padding: 5px;">Charges Payable By:</th><td style="border: 0.5px solid black; padding: 5px;">{documento_serializer.data["fk_vuelo"]["ente_pagador"]}</td></tr>\n'

                message += f'  <tr style="border: 0.5px solid black;"><th style="border: 0.5px solid black; padding: 5px;">Flight No.:</th><td style="border: 0.5px solid black; padding: 5px;">{documento_serializer.data["fk_vuelo"]["numero_vuelo"]}</td><th style="border: 0.5px solid black; padding: 5px;">Aircraft Reg:</th><td style="border: 0.5px solid black; padding: 5px;">{documento_serializer.data["fk_vuelo"]["ac_reg"]}</td></tr>\n'

                message += f'  <tr style="border: 0.5px solid black;"><th style="border: 0.5px solid black; padding: 5px;">Routing:</th><td style="border: 0.5px solid black; padding: 5px;">{documento_serializer.data["fk_vuelo"]["lugar_salida"]["codigo"]}/{documento_serializer.data["fk_vuelo"]["lugar_destino"]["codigo"]}</td><th style="border: 0.5px solid black; padding: 5px;">Flight Type:</th><td style="border: 0.5px solid black; padding: 5px;">{documento_serializer.data["fk_vuelo"]["tipo_vuelo"]["nombre"]}</td></tr>\n'

                message += f'  <tr style="border: 0.5px solid black;"><th style="border: 0.5px solid black; padding: 5px;">Gate/Gate:</th><td style="border: 0.5px solid black; padding: 5px;">{documento_serializer.data["fk_vuelo"]["gate"]}</td><th style="border: 0.5px solid black; padding: 5px;">AircraftType:</th><td style="border: 0.5px solid black; padding: 5px;">{documento_serializer.data["fk_vuelo"]["ac_type"]}</td></tr>\n'

                message += f'  <tr style="border: 0.5px solid black;"><th style="border: 0.5px solid black; padding: 5px;">ETA:</th><td style="border: 0.5px solid black; padding: 5px;">{documento_serializer.data["fk_vuelo"]["ETA"]} - {documento_serializer.data["fk_vuelo"]["ETA_fecha"]}</td><th style="border: 0.5px solid black; padding: 5px;">ETD:</th><td style="border: 0.5px solid black; padding: 5px;">{documento_serializer.data["fk_vuelo"]["ETD"]} - {documento_serializer.data["fk_vuelo"]["ETD_fecha"]}</td></tr>\n'

                message += f'</table>\n'
                message += f'<p>Tareas realizadas:</p>\n'
                message += f'{formatted_data}</body></html>\n'

                message += f'<p style=color: #D5D8DC >*Esto es un reporte preliminar, el documento oficial será enviado posteriormente por Siaca*</p>\n'

                from_email = settings.EMAIL_HOST_USER
                to_email = [documento_serializer.data["fk_vuelo"]["fk_aerolinea"]["correo"],documento_serializer.data["fk_vuelo"]["fk_aerolinea"]["correo_secundario"]]

                email = EmailMultiAlternatives(subject, message, from_email, to_email)
                email.attach_alternative(message, "text/html")
                email.send()

                # Return the data as before
                return Response({"mensaje enviado"}, status=status.HTTP_200_OK)
            else:
                 return Response({"mensaje no enviado"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)
        

class UpdateHora(generics.RetrieveUpdateDestroyAPIView):

        #Modificar subtarea de Hora de inicio
        def patch(self, request, pk=None, *args, **kwargs):
            token = request.GET.get('token')
            token = Token.objects.filter(key = token).first()
            if token:
                hora = Hora.objects.filter(id = pk).first()
                if hora:
                    hora_serializer = HoraInicioSerializer(hora, data=request.data)
                    if hora_serializer.is_valid():
                        hora_serializer.save()
                        return Response(hora_serializer.data, status=status.HTTP_200_OK)
                return Response({'mensaje':'No existe la subtarea'}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)


class UpdateHoraInicioFin(generics.RetrieveUpdateDestroyAPIView):

        #Modificar subtarea de Hora de inicio y fin
        def patch(self, request, pk=None, *args, **kwargs):
            token = request.GET.get('token')
            token = Token.objects.filter(key = token).first()
            if token:
                hora = HoraInicioFin.objects.filter(id = pk).first()
                if hora:
                    hora_serializer = HoraInicioFinSerializer(hora, data=request.data)
                    if hora_serializer.is_valid():
                        hora_serializer.save()
                        return Response(hora_serializer.data, status=status.HTTP_200_OK)
                return Response({'mensaje':'No existe la subtarea'}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)
        

class UpdateComentario(generics.RetrieveUpdateDestroyAPIView):

        #Modificar comentario
        def patch(self, request, pk=None, *args, **kwargs):
            token = request.GET.get('token')
            token = Token.objects.filter(key = token).first()
            if token:
                comentario = Comentario.objects.filter(id = pk).first()
                if comentario:
                    comentario_serializer = ComentarioSerializer(comentario, data=request.data)
                    if comentario_serializer.is_valid():
                        comentario_serializer.save()
                        return Response(comentario_serializer.data, status=status.HTTP_200_OK)
                return Response({'mensaje':'No existe el comentario'}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)


class UpdateCodigoDemora(generics.RetrieveUpdateDestroyAPIView):

    #Modificar codigo de demora
    def patch(self, request, pk=None, *args, **kwargs):
        token = request.GET.get('token')
        token = Token.objects.filter(key=token).first()
        if token:
            codigo = turnaround.objects.filter(id=pk).first()
            if codigo:
                codigo_demora = codigos_demora.objects.filter(id=request.data.get('fk_codigos_demora_id')).first()
                if codigo_demora:
                    codigo_serializer = CodigoSerializer(codigo, data=request.data)
                    if codigo_serializer.is_valid():
                        codigo_serializer.save(fk_codigos_demora=codigo_demora)
                        return Response(codigo_serializer.data, status=status.HTTP_200_OK)
                return Response({'mensaje':'No existe el codigo de demora'}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'mensaje':'No existe el turnaround'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)