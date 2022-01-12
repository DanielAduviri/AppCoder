from django.shortcuts import render
from modulo1.models import Curso
from django.http import HttpResponse

def crea_curso(self,nombre, camada):

    nuevo_curso= Curso(nombre= nombre, camada=camada)
    nuevo_curso.save()

    return HttpResponse(f'Se creo el curso de {nuevo_curso.nombre} con el nro de camada de {nuevo_curso.camada} ')
#En la linea 9 podria hacer lo de crear un  template especifico para esta view y asi como hicimos en CRUD, etc pero para
#hacerlo más rápido usamos el httpresponsedd

def inicio(req):
    return render(req, 'inicio.html')
    #Para que una vista pueda mostrar un template una vez llamada hay VARIAS formas de hacerlo como con el
    #Context, los cargadores, etc. Todas sirven para lo mismo

def curso(req):
    return render(req,'curso.html')

def profesores(req):
    return render(req, 'profesores.html')

def estudiantes(req):
    return render(req, 'estudiantes.html')

def entregables(req):
    return render(req, 'entregables.html')
