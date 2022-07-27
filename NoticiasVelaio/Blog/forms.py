import django
from django import forms
from django.forms import ModelForm, TextInput
from .models import City

class usuario_form(forms.Form):
    nombre = forms.CharField(max_length=30, required=True)
    contrasena = forms.CharField(max_length=30, required=True)

class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['name']
        widgets = {
            'name': TextInput(attrs={'class' : 'input', 'placeholder' : 'Ciudad'}),
        } 