from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.sessions.models import Session
import datetime

class Login(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        login_serializer = self.serializer_class(data = request.data, context = {'request':request})
        if login_serializer.is_valid():
            user = login_serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user = user)
            if created:
                return Response({
                    'token': token.key,
                    'mensaje': 'Inicio de sesión exitoso'
                })
            else: 
                token.delete()
                token = Token.objects.create(user = user)
                return Response({
                    'token': token.key,
                    'mensaje': 'Inicio de sesión exitoso'
                })
                
        return Response({'mensaje':'Hola desde response'}, status = status.HTTP_200_OK)

class Logout(APIView):

    def get(self, request, *args, **kwargs):
        
            token = request.GET.get('token')
            token = Token.objects.filter(key = token).first()
            if token:
                user = token.user
                all_sessions = Session.objects.filter(expire_date = datetime.datetime.now())
                if all_sessions.exists():
                    for session in all_sessions:
                        session_data = session.get_decoded()
                        if user.id == int(session_data.get('_auth_user_id')):
                            session.delete()
                session_message = 'Sesión eliminada'
                token.delete()
                token_message = 'Token elimindo'

                return Response({'token_message': token_message,
                                'session_message': session_message})
            
       
            return Response({'Error': 'error'})