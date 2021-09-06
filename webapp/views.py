from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def bienvenido(request):
    return HttpResponse('Hola mundo desde DJango')

def despedirse(request):
    return HttpResponse('Nos vemos')

def contacto(request):
    return HttpResponse('Error: 404, Page not found')