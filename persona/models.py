from django.db import models
# ORM: Object Relational Mapping 
# SQL(Statement) -> Python Object 


# Clase de modelo, agregamos primero la clase porque no se va a relacionar con otro clase
class Domicilio(models.Model):
    calle = models.CharField(max_length=255)
    no_calle = models.IntegerField()
    pais = models.CharField(max_length=255)

    # Personalizar el ID
    def __str__(self):
        return f'Domicilio {self.id}: {self.calle} {self.no_calle} {self.pais}'

# Llave foranea para relacionar la clase domicilio con
# la clase Persona

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=255) # Ind. max de caracteres max_lenght
    apellido = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    # Llave foranea 
    domicilio = models.ForeignKey(Domicilio, on_delete=models.SET_NULL, null=True)

    # Persolanizar el ID
    def __str__(self):
        return f'Persona {self.id}: {self.nombre} {self.email}'
        
