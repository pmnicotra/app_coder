from django.shortcuts import render
from django.http import HttpResponse
from app_coder.models import Curso
# Create your views here.

def curso(self):

    curso = Curso(nombre = "Python", camada = "37190")

    curso.save()
    
    documento = f"El curso es: {curso.nombre}, camada: {curso.camada}"
    
    return HttpResponse(documento)

def inicio(request):

    return render(request, "app_coder/inicio.html")


def cursos(request):

    return render(request, "app_coder/cursos.html")

def profesores(request):

    return render(request, "app_coder/profesores.html")

def estudiantes(request):

    return render(request, "app_coder/estudiantes.html")

def entregables(request):

    return render(request, "app_coder/entregables.html")
