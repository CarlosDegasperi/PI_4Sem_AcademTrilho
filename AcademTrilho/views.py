from django.shortcuts import render
from .models import Curso, Semestre

def consultar_cursos_semestres(request):
    cursos = Curso.objects.all()
    semestres = Semestre.objects.all()
    return render(request, 'consultar.html', {'cursos': cursos, 'semestres': semestres})
