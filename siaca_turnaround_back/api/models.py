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
    estado=models.CharField(max_length=50)
    fk_categoria=models.ForeignKey(categoria,blank=True,null=True,on_delete=models.CASCADE)
    imagen=models.CharField(max_length=50)

class codigos_demora(models.Model):
    identificador=models.PositiveIntegerField()
    alpha=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=50)
    categoria=models.CharField(max_length=50)
    departamento=models.CharField(max_length=50)
    accountable=models.CharField(max_length=50)

class aerolinea(models.Model):
    nombre=models.CharField(max_length=50)
    correo=models.CharField(max_length=50)
    telefono=models.CharField(max_length=50)
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

class vuelo(models.Model):
    fk_aerolinea=models.ForeignKey(aerolinea,blank=True,null=True,on_delete=models.CASCADE)
    fk_plantilla=models.ForeignKey(plantilla,blank=True,null=True,on_delete=models.CASCADE)
    ac_reg=models.CharField(max_length=50)
    ac_type=models.CharField(max_length=50)
    estado=models.CharField(max_length=50)
    lugar_salida=models.CharField(max_length=50)
    lugar_destino=models.CharField(max_length=50)
    fecha_llegada=models.DateField()
    hora_llegada=models.DateTimeField()
    ente_pagador=models.CharField(max_length=50)
    numero_vuelo=models.BigIntegerField()
    ETA=models.CharField(max_length=50)
    ETD=models.CharField(max_length=50)
    ATA=models.CharField(max_length=50)
    ATD=models.CharField(max_length=50)
    gate=models.CharField(max_length=50)
    tipo_vuelo=models.CharField(max_length=50)

class turnaround(models.Model):
    identificador=models.PositiveIntegerField()
    fk_vuelo=models.ForeignKey(vuelo,blank=True,null=True,on_delete=models.CASCADE)
    fk_codigos_demora=models.ForeignKey(codigos_demora,blank=True,null=True,on_delete=models.CASCADE)
    fecha_inicio=models.DateField()
    fecha_fin=models.DateField()

class maquinaria_turnaround(models.Model):
    fk_turnaround=models.ForeignKey(turnaround,blank=True,null=True,on_delete=models.CASCADE)
    fk_maquinaria=models.ForeignKey(maquinaria,blank=True,null=True,on_delete=models.CASCADE)

class usuario_turnaround(models.Model):
    fk_turnaround=models.ForeignKey(turnaround,blank=True,null=True,on_delete=models.CASCADE)
    fk_user=models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE)

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
