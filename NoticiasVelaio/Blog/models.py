from django.db import models

# Create your models here.
class usuario (models.Model):

    nombre= models.CharField(max_length=30)
    contrasena= models.CharField(max_length=300) 
    class Meta:
        db_table = "usuario"

