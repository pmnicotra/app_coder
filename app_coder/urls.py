from django.urls import path

from app_coder import views
from app_coder.views import curso_formulario
from app_coder.views import prof_formulario
from app_coder.views import buscar

urlpatterns = [
   
    path('', views.inicio, name="Inicio"), #esta era nuestra primer view
    path('cursos', views.cursos, name="Cursos"),
    path('profesores', views.profesores, name="Profesores"),
    path('estudiantes', views.estudiantes, name="Estudiantes"),
    path('entregables', views.entregables, name="Entregables"),
    path('curso_formulario', views.curso_formulario, name="Curso_Formulario"),
    path('profesor_formulario', views.prof_formulario, name="Profe_Formulario"),
    path('buscar/', views.buscar),
]

