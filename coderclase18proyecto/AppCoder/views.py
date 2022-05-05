from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader,Template,Context
from AppCoder.models import Familiares

# Create your views here.

def familiares (self):

    familiar1 = Familiares(nombre="martin",apellido="quinteiro",edad=38,nacimiento="1983-07-04")
    familiar1.save()
#    documentoDeTexto = f"-----> el familiar es {familiar1.nombre} {familiar1.apellido}, tiene {familiar1.edad} años y nació el {familiar1.nacimiento}"
#    return HttpResponse(documentoDeTexto)

    familiar2 = Familiares(nombre="felicitas",apellido="quinteiro",edad=5,nacimiento="2017-07-28")
    familiar2.save()
 #   documentoDeTexto = f"-----> el familiar es {familiar2.nombre} {familiar2.apellido}, tiene {familiar2.edad} años y nació el {familiar2.nacimiento}"
 #   return HttpResponse(documentoDeTexto)

    familiar3 = Familiares(nombre="alfredo",apellido="quinteiro",edad=2,nacimiento="2020-04-27")
    familiar3.save()
    documentoDeTexto = {"familiar1":familiar1,"familiar2":familiar2,"familiar3":familiar3}
    return HttpResponse(documentoDeTexto)

#def familiares2 (request):
 #   return render(request,"AppCoder/familiares.html")

def templatefamiliares (request):

    familiar1 = Familiares(nombre="martin",apellido="quinteiro",edad=38,nacimiento="1983-07-04")
    familiar1.save()
#    documentoDeTexto = f"-----> el familiar es {familiar1.nombre} {familiar1.apellido}, tiene {familiar1.edad} años y nació el {familiar1.nacimiento}"
#    return HttpResponse(documentoDeTexto)

    familiar2 = Familiares(nombre="felicitas",apellido="quinteiro",edad=5,nacimiento="2017-07-28")
    familiar2.save()
 #   documentoDeTexto = f"-----> el familiar es {familiar2.nombre} {familiar2.apellido}, tiene {familiar2.edad} años y nació el {familiar2.nacimiento}"
 #   return HttpResponse(documentoDeTexto)

    familiar3 = Familiares(nombre="alfredo",apellido="quinteiro",edad=2,nacimiento="2020-04-27")
    familiar3.save()


    diccionario = {"familiar1":familiar1,"familiar2":familiar2,"familiar3":familiar3}
    plantilla = loader.get_template("familiares.html")
#    mihtml.close()
 #   micontexto = Context(diccionario)
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)