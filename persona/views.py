from django.shortcuts import get_object_or_404, render
from django.forms import modelform_factory
# Create your views here.
from persona.models import Persona

def detallePersonas(request, id):
    # persona = Persona.objects.get(pk = id)
    # When don't have a user that not exits
    persona = get_object_or_404(Persona, pk=id)
    return render(request, 'personas/detalle.html', {'persona': persona})

PersonaForm = modelform_factory(Persona, exclude=[]) # Para generar objecto d formulario

def nuevaPersona(request):
    # Crear object persona form
    formaPersona = PersonaForm()
    return render(request, 'personas/nuevo.html', {'formaPersona':formaPersona})
