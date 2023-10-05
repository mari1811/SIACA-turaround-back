from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class usuario(models.Model):
    fk_user=models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE)
    cedula=models.BigIntegerField()
    cargo=models.CharField(max_length=50)
    departamento=models.CharField(max_length=50)
    telefono=models.CharField(max_length=50)
    turno=models.CharField(max_length=50)

class categoria(models.Model):
    nombre=models.CharField(max_length=100)

class maquinaria(models.Model):
    identificador=models.CharField(max_length=50)
    modelo=models.CharField(max_length=50)
    combustible=models.CharField(max_length=50)
    estado=models.BooleanField(null=True)
    fk_categoria=models.ForeignKey(categoria,blank=True,null=True,on_delete=models.CASCADE)
    imagen=models.CharField(max_length=50, null=True)

class codigos_demora(models.Model):
    identificador=models.PositiveIntegerField()
    alpha=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=500)
    categoria=models.CharField(max_length=50)
    departamento=models.CharField(max_length=50)
    accountable=models.CharField(max_length=50)

class aerolinea(models.Model):
    nombre=models.CharField(max_length=50)
    correo=models.CharField(max_length=50)
    telefono=models.CharField(max_length=50)
    telefono_secundario=models.CharField(max_length=50, null=True)
    correo_secundario=models.CharField(max_length=50, null=True)
    pais=models.CharField(max_length=50, null=True)
    ciudad=models.CharField(max_length=50, null=True)
    codigo=models.CharField(max_length=50)
    imagen=models.ImageField(upload_to="images/", null=True, blank=True)

class plantilla(models.Model):
    titulo=models.CharField(max_length=50)

class tarea(models.Model):
    fk_plantilla=models.ForeignKey(plantilla,blank=True,null=True,on_delete=models.CASCADE)
    titulo=models.CharField(max_length=50)

class tipo(models.Model):
    nombre=models.CharField(max_length=50)

class subtarea(models.Model):
    fk_tarea=models.ForeignKey(tarea,blank=True,null=True,on_delete=models.CASCADE)
    titulo=models.CharField(max_length=50)
    fk_tipo=models.ForeignKey(tipo,blank=True,null=True,on_delete=models.CASCADE)

class tipo_subtarea(models.Model):
    fk_tipo=models.ForeignKey(tipo,blank=True,null=True,on_delete=models.CASCADE)
    fk_subtarea=models.ForeignKey(subtarea,blank=True,null=True,on_delete=models.CASCADE)

class cantidad_categoria(models.Model):
    cantidad=models.IntegerField()
    fk_categoria=models.ForeignKey(categoria,blank=True,null=True,on_delete=models.CASCADE)
    fk_plantilla=models.ForeignKey(plantilla,blank=True,null=True,on_delete=models.CASCADE)

class ciudades(models.Model):
    nombre=models.CharField(max_length=50,blank=True,null=True)
    codigo=models.CharField(max_length=50,blank=True,null=True)
    codigo_oaci=models.CharField(max_length=50,blank=True,null=True)
    pais=models.CharField(max_length=50,blank=True,null=True)
    aeropuerto=models.CharField(max_length=100,blank=True,null=True)

class tipo_vuelo(models.Model):
    nombre=models.CharField(max_length=50)

class tipo_servicio(models.Model):
    nombre=models.CharField(max_length=50)

class vuelo(models.Model):
    fk_aerolinea=models.ForeignKey(aerolinea,blank=True,null=True,on_delete=models.CASCADE)
    fk_plantilla=models.ForeignKey(plantilla,blank=True,null=True,on_delete=models.CASCADE)
    stn=models.ForeignKey(ciudades,blank=True,null=True,on_delete=models.CASCADE,related_name='ciudades_stn')
    ac_reg=models.CharField(max_length=50, blank=True,null=True)
    ac_type=models.CharField(max_length=50, blank=True,null=True)
    estado=models.CharField(max_length=50, blank=True,null=True)
    lugar_salida=models.ForeignKey(ciudades,blank=True,null=True,on_delete=models.CASCADE,related_name='ciudades_salida')
    lugar_destino=models.ForeignKey(ciudades,blank=True,null=True,on_delete=models.CASCADE,related_name='ciudades_destino')
    ente_pagador=models.CharField(max_length=50, blank=True,null=True)
    numero_vuelo=models.CharField(max_length=50, blank=True,null=True)
    ETA=models.TimeField(blank=True,null=True)
    ETD=models.TimeField(blank=True,null=True)
    ETA_fecha=models.DateField(blank=True,null=True)
    ETD_fecha=models.DateField(blank=True,null=True)
    ATA=models.TimeField(blank=True,null=True)
    ATD=models.TimeField(blank=True,null=True)
    ATA_fecha=models.DateField(blank=True,null=True)
    ATD_fecha=models.DateField(blank=True,null=True)
    gate=models.PositiveIntegerField(blank=True,null=True)
    tipo_vuelo=models.ForeignKey(tipo_vuelo,blank=True,null=True,on_delete=models.CASCADE)
    tipo_servicio=models.ForeignKey(tipo_servicio,blank=True,null=True,on_delete=models.CASCADE)
    icao_hex=models.CharField(max_length=50, blank=True,null=True)

class turnaround(models.Model):
    identificador=models.PositiveIntegerField(blank=True,null=True)
    fk_vuelo=models.ForeignKey(vuelo,blank=True,null=True,on_delete=models.CASCADE)
    fk_codigos_demora=models.ForeignKey(codigos_demora,blank=True,null=True,on_delete=models.CASCADE)
    hora_inicio=models.TimeField(blank=True,null=True)
    hora_fin=models.TimeField(blank=True,null=True)
    fecha_inicio=models.DateField(blank=True,null=True)
    fecha_fin=models.DateField(blank=True,null=True)

class maquinaria_historial(models.Model):
    fk_maquinaria=models.ForeignKey(maquinaria,blank=True,null=True,on_delete=models.CASCADE)
    hora_inicio=models.TimeField(blank=True,null=True)
    hora_fin=models.TimeField(blank=True,null=True)
    fecha=models.DateField(blank=True,null=True)
    fk_turnaround=models.ForeignKey(turnaround,blank=True,null=True,on_delete=models.CASCADE)

class usuario_turnaround(models.Model):
    fk_turnaround=models.ForeignKey(turnaround,blank=True,null=True,on_delete=models.CASCADE)
    fk_usuario=models.ForeignKey(usuario,blank=True,null=True,on_delete=models.CASCADE)
    hora_inicio=models.TimeField(blank=True,null=True)
    hora_fin=models.TimeField(blank=True,null=True)
    fecha=models.DateField(blank=True,null=True)

class Imagen(models.Model):
    fk_turnaround=models.ForeignKey(turnaround,blank=True,null=True,on_delete=models.CASCADE)
    fk_subtarea=models.ForeignKey(subtarea,blank=True,null=True,on_delete=models.CASCADE)
    link=models.CharField(max_length=200)

class Hora(models.Model):
    fk_turnaround=models.ForeignKey(turnaround,blank=True,null=True,on_delete=models.CASCADE)
    fk_subtarea=models.ForeignKey(subtarea,blank=True,null=True,on_delete=models.CASCADE)
    hora_inicio=models.DateTimeField()

class HoraInicioFin(models.Model):
    fk_turnaround=models.ForeignKey(turnaround,blank=True,null=True,on_delete=models.CASCADE)
    fk_subtarea=models.ForeignKey(subtarea,blank=True,null=True,on_delete=models.CASCADE)
    hora_inicio=models.DateTimeField()
    hora_fin=models.DateTimeField()

class Comentario(models.Model):
    fk_turnaround=models.ForeignKey(turnaround,blank=True,null=True,on_delete=models.CASCADE)
    fk_subtarea=models.ForeignKey(subtarea,blank=True,null=True,on_delete=models.CASCADE)
    comentario=models.CharField(max_length=200)

class documento(models.Model):
    fk_vuelo=models.ForeignKey(vuelo,blank=True,null=True,on_delete=models.CASCADE)
    fecha=models.DateTimeField()
    link=models.CharField(max_length=200)
