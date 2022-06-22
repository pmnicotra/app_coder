from django import forms

class Curso_Formulario(forms.Form):
    curso = forms.CharField()
    camada = forms.IntegerField()

class Prof_Formulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    profesion = forms.CharField(max_length=30)
    


