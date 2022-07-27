from django.urls import path
from . import views

urlpatterns = [
    path('noticias/', views.noticias),
    path('tiempo/', views.tiempo)
]