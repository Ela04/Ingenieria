
from django.shortcuts import render

from .models import Alumno,Genero, Cursos

# Create your views here.


def index(request):
    alumnos= Alumno.objects.all()
    context={"alumnos":alumnos}
    return render(request, 'alumnos/index.html', context)


def listadoSQL(request):
    alumnos= Alumno.objects.raw('SELECT * FROM alumnos_alumno')
    print(alumnos)
    context={"alumnos":alumnos}
    return render(request, 'alumnos/listadoSQL.html', context)

def base(request):
    return render(request, 'alumnos/base.html')

def home(request):
    return render(request, 'alumnos/home.html')

def nosotros(request):
    return render(request, 'alumnos/nosotros.html')

def contacto(request):
    return render(request, 'alumnos/contacto.html')
    
def cursos(request):
    return render(request, 'alumnos/cursos.html')
