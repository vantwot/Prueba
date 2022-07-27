from django.shortcuts import render
import requests
from django.shortcuts import render, get_object_or_404
from Blog.models import *
from django.http import JsonResponse
from .forms import *
from django.contrib.auth.hashers import make_password, check_password
from .models import City
from .forms import CityForm

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

            return JsonResponse(True, safe=False)
        else:
            return JsonResponse(False, safe=False)
    return JsonResponse(False, safe=False)

def login(request):
    return render(request, 'login.html')

def noticias(request):
    url = 'https://newsapi.org/v2/everything?q=Cryptocurrency&from=2022-07-26&sortBy=popularity&apiKey=5aeb68fdf65048cc918a20f6d34b2cbd'

    crypto_news = requests.get(url).json()

    a = crypto_news['articles']
    desc =[]
    title =[]
    img =[]

    for i in range(len(a)):
        f = a[i]
        title.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    mylist = zip(title, desc, img)

    context = {'mylist': mylist}

    return render(request, 'noticias.html', context)

def tiempo(request):
    cities = City.objects.all()
    url = 'https://api.openweathermap.org/data/2.5/weather?zip=94040,us&appid=ca3787dfdd32f98a1c9b5fd365b02188'
    
    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    weather_data = []

    for city in cities:
        city_weather = requests.get(url.format(city)).json()

        weather = {
            'city' : city,
            #'temperature' : city_weather['main']['temp'],
            'description' : city_weather['weather'][0]['description'],
            'icon' : city_weather['weather'][0]['icon'],
            'humidity': city_weather['main']['humidity'],
            'pressure': city_weather['main']['pressure'],
            'country': city_weather['sys']['country'],
            'sunrise': city_weather['sys']['sunrise'],
            'sunset': city_weather['sys']['sunset'],
            'windspeed': city_weather['wind']['speed']
        }

        weather_data.append(weather)

    context = {'weather_data': weather_data, 'form': form}

    return render(request, 'tiempo.html', context)