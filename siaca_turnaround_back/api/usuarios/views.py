from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status,generics, viewsets, response
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.sessions.models import Session
import datetime
from api.usuarios.api.serializer import ResetPasswordSerializer, EmailSerializer
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.core.mail import EmailMultiAlternatives
from django.conf import settings




from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode



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
    



class PasswordReset(generics.GenericAPIView):
    """
    Request for Password Reset Link.
    """

    serializer_class = EmailSerializer

    def post(self, request):
        """
        Create token.
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.data["email"]
        user = User.objects.filter(username=email).first()
        if user:
            encoded_pk = urlsafe_base64_encode(force_bytes(user.pk))
            token = PasswordResetTokenGenerator().make_token(user)
            reset_url = reverse(
                "reset-password",
                kwargs={"encoded_pk": encoded_pk, "token": token},
            )
            reset_link = f"localhost:8000{reset_url}"

            msg = EmailMultiAlternatives(
            'Cambio de contraseña',
            'Ingrese a este link para cambiar su contraseña:\n{}'.format(reset_link),
            settings.EMAIL_HOST_USER,
            [email]
        )
            msg.send()

            # send the rest_link as mail to the user.

            return response.Response(
                {
                    "message": 
                    f"Your password rest link: {reset_link}"
                },
                status=status.HTTP_200_OK,
            )
        else:
            return response.Response(
                {"message": "User doesn't exists"},
                status=status.HTTP_400_BAD_REQUEST,
            )


class ResetPasswordAPI(generics.GenericAPIView):
    """
    Verify and Reset Password Token View.
    """

    serializer_class = ResetPasswordSerializer

    def patch(self, request, *args, **kwargs):
        """
        Verify token & encoded_pk and then reset the password.
        """
        serializer = self.serializer_class(
            data=request.data, context={"kwargs": kwargs}
        )
        serializer.is_valid(raise_exception=True)
        return response.Response(
            {"message": "Password reset complete"},
            status=status.HTTP_200_OK,
        )