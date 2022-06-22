from django.shortcuts import render
from django.http import HttpResponse
from app_coder.forms import Curso_Formulario, Prof_Formulario
from app_coder.models import Curso, Profesor

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

def curso_formulario(request):

    if request.method == 'POST':

        mi_formulario = Curso_Formulario(request.POST)  #aquí mellega toda la información del html


        print(mi_formulario)

        if mi_formulario.is_valid:  #Si pasó la validación de Django

            informacion = mi_formulario.cleaned_data

            curso = Curso(nombre=informacion['curso'], camada=informacion['camada'])
            
            curso.save()

            return render(request, 'app_coder/inicio.html') #Vuelvo al inicio o a donde quieran


    else:
        mi_formulario = Curso_Formulario()  #Formulario vacio para construir el html

    return render(request, 'app_coder/curso_formulario.html', {'mi_formulario':mi_formulario})

def prof_formulario(request):

    if request.method == "POST":

        mi_formulario = Prof_Formulario(request.POST)
        print(mi_formulario)

        if mi_formulario.is_valid:

            informacion = mi_formulario.cleaned_data
            profesor = Profesor(nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'], profesion=informacion['profesion'])
            profesor.save()

            return render(request, 'app_coder/inicio.html')

    else:
        mi_formulario = Prof_Formulario()

    return render(request, 'app_coder/profesor_formulario.html', {'mi_formulario':mi_formulario})

def buscar(request):

      if request.GET["camada"]: #if request.method == 'Get':

	      #respuesta = f"Estoy buscando la camada nro: {request.GET['camada'] }" 
            camada = request.GET['camada'] 
            print(camada)
            cursos = Curso.objects.filter(camada__icontains=camada)
            print(cursos)
            return render(request, "app_coder/inicio.html", {"cursos":cursos, "camada":camada})

      else: 

	      respuesta = "No enviaste datos"

      return render(request,"app_coder/inicio.html", {"respuesta":respuesta})
        