from django.contrib import admin
from persona.models import Domicilio, Persona
# Register your models here.
# Registe the model class that we need to register

admin.site.register(Persona)
admin.site.register(Domicilio)