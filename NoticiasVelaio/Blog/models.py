from django.db import models

# Create your models here.
class usuario (models.Model):

    nombre= models.CharField(max_length=30)
    contrasena= models.CharField(max_length=300) 
    class Meta:
        db_table = "usuario"

class City(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self): #show the actual city name on the dashboard
        return self.name
    
    class Meta: 
        verbose_name_plural = 'cities'