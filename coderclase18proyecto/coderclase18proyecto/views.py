from pipes import Template
from django.http import HttpResponse
import datetime
from django.template import Context, Template, loader

def saludo (request):
    return HttpResponse("Hola Django Coder clase18")

def diaDeHoy (rquest):
    dia = datetime.datetime.now()
    fechahoy = f"Hoy es dia: <br> {dia}"
    return HttpResponse (fechahoy)

def minombre (self, nombre):
    documentoDeTexto = f"Mi nombre es: <br><br> {nombre}"
    return HttpResponse (documentoDeTexto)

def probandotemplate (self):
    
    nom = "martin"
    ap = "quinteiro"
    listaDeNotas = [2,3,4,3,2,6,8,7,9,8]
    diccionario = {"nombre":nom, "apellido":ap,"notas":listaDeNotas}

    
#    mihtml = open("C:/Users/l0271969/OneDrive - Banco de Galicia Y Buenos Aires S.A/Martín/PY/Coder/clase18/coderclase18/coderclase18proyecto/plantillas/template1.html")
#    plantilla = Template(mihtml.read())
    plantilla = loader.get_template("template1.html")
#    mihtml.close()
 #   micontexto = Context(diccionario)
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)