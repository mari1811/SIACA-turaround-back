from django.urls import path
from .api import usuario_api_view, UserListView, registro_usuario, Lista, Prueba, Update, DeleteUser, EstadoUsuario, Solicitudes, Contador, UsuarioHistorial, MetricaTurnaroundPersonal, Departamento, Cargo, UsuarioTurnaround
from api.usuarios.views import Login, Logout, PasswordReset, ResetPasswordAPI
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns=[

    #POST: Inicio de sesión http://127.0.0.1:8000/usuarios/login/
    path('login/', Login.as_view(), name='Login'),

    #GET: Cerrar sesión http://127.0.0.1:8000/usuarios/logout/?token=
    path('logout/', Logout.as_view(), name='Logout'),

    #POST: Registro de usuario PASO 1  http://127.0.0.1:8000/usuarios/registro/
    path('registro/', usuario_api_view, name='usuario_api_view'),

    #PATCH: Edita nombre y apellido en el registro con el ID http://127.0.0.1:8000/usuarios/registro2user2/<ID>/
    path('registro2user2/<int:pk>/', Update.as_view(), name='update'),

    #POST: Registro de usuario PASO 2 http://127.0.0.1:8000/usuarios/registro2usuario/
    path('registro2usuario/', registro_usuario, name='registro_usuario'),

    #GET: Lista de usuarios http://127.0.0.1:8000/usuarios/lista/?token=
    path('lista/', Lista.as_view(), name='lista'),

    #GET: Lista de departamentos http://127.0.0.1:8000/usuarios/departamentos/
    path('departamentos/', Departamento.as_view(), name='departamentos_usuarios'),

    #GET: Lista de cargos http://127.0.0.1:8000/usuarios/cargos/
    path('cargos/', Cargo.as_view(), name='cargos_usuarios'),

    #DELETE: Eliminar usuario http://127.0.0.1:8000/usuarios/listado/<ID>/?token=
    path('eliminar/<int:pk>/', DeleteUser.as_view(), name='eliminar_usuario'),

    #GET: buscar usuario por su username http://127.0.0.1:8000/usuarios/listado/user/?search=
    path('listado/user/', UserListView.as_view(), name='user_api_view'),

    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    #POST: Recuperar clave http://127.0.0.1:8000/usuarios/password-reset/
    path('password-reset/', PasswordReset.as_view(), name ="request-password-reset"),

    #PATCH: Nueva clave (link que llega por correo)
    path('password-reset/<str:encoded_pk>/<str:token>', ResetPasswordAPI.as_view(), name ="reset-password"),

    path('prueba/', Prueba.as_view(), name='prueba'),

    #PATCH: Cambia el estado del usuario http://127.0.0.1:8000/usuarios/estado/<ID>/?token=
    path('estado/<int:pk>/', EstadoUsuario.as_view(), name='estado_usuario'),

    #GET: Lista de solicitudes http://127.0.0.1:8000/usuarios/solicitudes/?token=
    path('solicitudes/', Solicitudes.as_view(), name='solicitudes_usuario'),

    #GET: Contador de solicitudes http://127.0.0.1:8000/usuarios/contador-solicitudes/?token=
    path('contador-solicitudes/', Contador.as_view(), name='solicitudes_contador'),

    #GET: Lista de personal disponible http://127.0.0.1:8000/usuarios/reserva/AAAA-MM-DD/HoraInicio/HoraFin/?token=
    path('reserva/<str:fecha>/<str:horaI>/<str:horaF>/', UsuarioHistorial.as_view(), name='uausrio_reserva'),

    #POST: Asignar personal a turnaround http://127.0.0.1:8000/usuarios/reserva/?token=
    path('reserva/', UsuarioHistorial.as_view(), name='usuario_reserva_crear'),

    #GET: Metrica numero de turnarounds en los que ha estado el personal http://127.0.0.1:8000/usuarios/metrica/turnaround/?token=
    path('metrica/turnaround/', MetricaTurnaroundPersonal.as_view(), name='metrica_turnaround'),

    #GET: Personal asociado a turnarounds http://127.0.0.1:8000/usuarios/lista/<ID>/?token=
    path('lista/<int:pk>/', UsuarioTurnaround.as_view(), name='usuario_turnaround'),

]