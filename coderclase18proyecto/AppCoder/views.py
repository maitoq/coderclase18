from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from AppCoder.models import Familiares

# Create your views here.

def familiares (self):
    familiares = Familiares(nombre="martin",apellido="quinteiro",edad=38,nacimiento="1983-07-04")
    familiares.save()
    documentoDeTexto = f"-----> el familiar es {familiares.nombre} {familiares.apellido}, tiene {familiares.edad} años y nació el {familiares.nacimiento}"
    return HttpResponse(documentoDeTexto)

def familiares2 (request):
    return render(request,"AppCoder/familiares.html")

#def templatefamiliares (request):

 #   plantilla = loader.get_template("familiares.html")
#    mihtml.close()
 #   micontexto = Context(diccionario)
  #  documento = plantilla.render(diccionario)
 #   return HttpResponse(documento)