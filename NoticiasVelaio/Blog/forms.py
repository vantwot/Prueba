import django
from django import forms

class usuario_form(forms.Form):
    nombre = forms.CharField(max_length=30, required=True)
    contrasena = forms.CharField(max_length=30, required=True)