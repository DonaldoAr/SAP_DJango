from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from persona.models import Persona
def bienvenido(request):
    # Add a dictionary
    # mensajes = {'msg1': 'Valor mensaje1', 'msg2': 'Mensaje 2'}
    #return render(request, 'bienvenido.html', mensajes)
    no_personas_v = Persona.objects.count()
    personas = Persona.objects.all()
    return render(request, 'bienvenido.html', {'no_personas': no_personas_v, 'personas': personas})

