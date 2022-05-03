from django.http import HttpResponse
from django.shortcuts import render

from AppCoder.models import Familiares

# Create your views here.

def familiares (self):
    familiares = Familiares(nombre="martin",apellido="quinteiro",edad=38,nacimiento="1983-07-04")
    familiares.save()
    documentoDeTexto = f"-----> el familiar es {familiares.nombre} {familiares.apellido}, tiene {familiares.edad} años y nació el {familiares.nacimiento}"
    return HttpResponse(documentoDeTexto)

