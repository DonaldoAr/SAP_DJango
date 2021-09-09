""" Class for aks a consulting 
Para crear nuestro formulario de tipo persona
"""
from django.forms import ModelForm, fields, widgets, EmailInput

from persona.models import Domicilio, Persona
# We can change o personalizer 
class PersonaForm(ModelForm):
    class Meta: 
        model = Persona
        # Indicamos que vamos a utiliza todos los atribustos de nuetro obj tipo persona
        fields = '__all__' 
        # Diccionario, que tipo de dato van a tener los datos a nivel html
        widgets = {
            'email': EmailInput(attrs = {'tipe': 'email'}) # Tipo email
        }
"""
class DomicilioForm(ModelForm):
    class Meta: 
        model = Domicilio
        # Indicamos que vamos a utiliza todos los atribustos de nuetro obj tipo persona
        fields = '__all__' 
        # Diccionario, que tipo de dato van a tener los datos a nivel html
        widgets = {
            'no_calle': TextInput(attrs = {'tipe': 'number'}) # Tipo email
        }
"""
