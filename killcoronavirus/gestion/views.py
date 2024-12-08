from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Usuario  # Importamos el modelo Usuario

# Create your views here.
def index(request):
    return HttpResponse("Bienvenido al sistema KillCoronaVirus")  # Respuesta simple para la página principal

def lista_usuarios(request):
    usuarios = Usuario.objects.all()  # Obtenemos todos los usuarios
    return render(request, 'gestion/lista_usuarios.html', {'usuarios': usuarios})  # Renderizamos una plantilla

def crear_usuario(request):
    if request.method == "POST":
        # Recogemos los datos enviados desde el formulario
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        correo = request.POST.get('correo')
        usuario = request.POST.get('usuario')
        contraseña = request.POST.get('contraseña')
        tipo_usuario = request.POST.get('tipo_usuario')
        
        # Creamos el usuario en la base de datos
        Usuario.objects.create(
            nombre=nombre,
            apellido=apellido,
            correo=correo,
            usuario=usuario,
            contraseña=contraseña,
            tipo_usuario=tipo_usuario
        )
        
        # Redirigimos a la lista de usuarios
        return redirect('lista_usuarios')
    
    # Si es una petición GET, mostramos el formulario
    return render(request, 'gestion/crear_usuario.html')

    