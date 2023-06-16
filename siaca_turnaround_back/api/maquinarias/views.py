from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import MaquinariaSerializer
from api.models import maquinaria



class MaquinariaAPIView(APIView):

    def get(self,request):
        maquinarias = maquinaria.objects.all()
        maquinarias_serializer = MaquinariaSerializer(maquinarias, many = True)
        return Response (maquinarias_serializer.data)
