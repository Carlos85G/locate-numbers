from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
#

# Función excenta de revisión CSRF para respuesta
@csrf_exempt
def helloWorld(request):
    if request.method == "POST":
        return HttpResponse('Es una petición POST')

    # Petición GET predeterminada
    return HttpResponse('Hola, Mundo ;)')
