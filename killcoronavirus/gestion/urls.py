from django.urls import path
from . import views  # Importamos las vistas desde gestion/views.py

urlpatterns = [
    path('', views.index, name='index'),  # Ruta principal para la aplicación
    path('usuarios/', views.lista_usuarios, name='lista_usuarios'),  # Nueva ruta para la lista de usuarios
    path('usuarios/crear/', views.crear_usuario, name='crear_usuario'),  # Crear un nuevo usuario
]




