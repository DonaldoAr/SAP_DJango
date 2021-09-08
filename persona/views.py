from django.shortcuts import get_object_or_404, render

# Create your views here.
from persona.models import Persona

def detallePersonas(request, id):
    # persona = Persona.objects.get(pk = id)
    # When don't have a user that not exits
    persona = get_object_or_404(Persona, pk=id)
    return render(request, 'personas/detalle.html', {'persona': persona})