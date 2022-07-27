from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from Blog.models import *
from django.http import JsonResponse
from .forms import *
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.

############ INGRESOS DE USUARIOS ##############

def ingresar(request):

    if(request.POST["nombre_ingreso"] and request.POST["password"]):

        username_request = request.POST["nombre_ingreso"]
        var_usuario =get_object_or_404(usuario, nombre = username_request)
        contrasena_request =check_password( request.POST["password"],var_usuario.contrasena)

        if (contrasena_request == True):

            return JsonResponse(True, safe=False)
        
    return JsonResponse(False, safe=False)

def crear_usuario(request):

    datos = usuario_form()

    if (request.method == "POST"):
        datos = usuario_form(request.POST)

        if datos.is_valid():
            var_usuario = usuario()
            var_usuario.nombre = datos.cleaned_data['nombre']
            var_usuario.contrasena = make_password(datos.cleaned_data['contrasena'])

            var_usuario.save()
            print("hola")

            return JsonResponse(True, safe=False)
        else:
            return JsonResponse(False, safe=False)
    return JsonResponse(False, safe=False)

def login(request):
    return render(request, 'login.html')

