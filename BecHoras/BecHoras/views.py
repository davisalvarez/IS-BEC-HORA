#from django.shortcuts import render
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse('Hola Mundo')

def root_page(request):
    return HttpResponse('Ruta de la pagina')

def mandarDato(request, dato=100):
    nuevo = int(dato) * 0.5
    msg = "El dato mandado es %s: %d" % (dato, nuevo)

    return HttpResponse(msg)
