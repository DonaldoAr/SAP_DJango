from django.shortcuts import get_object_or_404, redirect, render
from django.forms import modelform_factory
# Create your views here.
from persona.models import Persona
from persona.forms import PersonaForm

def detallePersonas(request, id):
    # persona = Persona.objects.get(pk = id)
    # When don't have a user that not exits
    persona = get_object_or_404(Persona, pk=id)
    return render(request, 'personas/detalle.html', {'persona': persona})
# Para generar objecto d formulario
#PersonaForm = modelform_factory(Persona, exclude=[]) 


def nuevaPersona(request):
    # Ask a POST
    if request.method == 'POST':
        formaPersona = PersonaForm( request.POST )
        # Validar la informacion
        if formaPersona.is_valid():
            formaPersona.save()
            return redirect('index') # Run another time the main page
        """
        else:
            # Rederigimos y mostramos errores
            return render(request, 'personas/nuevo.html', {'formaPersona':formaPersona})    
        """
    else: #  Ask a GET
        # Crear object persona form
        formaPersona = PersonaForm()
    return render(request, 'personas/nuevo.html', {'formaPersona':formaPersona})

def editarPersona(request, id):
    persona = get_object_or_404(Persona, pk=id)
    # Ask a POST
    if request.method == 'POST':
        formaPersona = PersonaForm( request.POST, instance= persona ) # Update
        # Validar la informacion
        if formaPersona.is_valid():
            formaPersona.save() # It will funtion how a update and not how a insert
            return redirect('index') # Run another time the main page
        """
        else:
            # Rederigimos y mostramos errores
            return render(request, 'personas/nuevo.html', {'formaPersona':formaPersona})    
        """
    else: #  Ask a GET
        # Recibe un object persona form que ya fue creado
        formaPersona = PersonaForm(instance= persona )
    return render(request, 'personas/editar.html', {'formaPersona':formaPersona})


def eliminarPersona(request, id):
    persona = get_object_or_404(Persona, pk=id)
    if persona:
        persona.delete()
    return redirect('index')