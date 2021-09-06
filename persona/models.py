from django.db import models
# ORM: Object Relational Mapping 
# SQL(Statement) -> Python Object 

# Create your models here.
class Persona(models.Model):
    nombre= models.CharField(max_length=255) # Ind. max de caracteres max_lenght
    apellido= models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    # Persolanizar el ID
    def __str__(self):
        return f'Persona {self.id}: {self.nombre} {self.email}'
        
