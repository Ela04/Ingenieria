from django.contrib import admin
from .models import Alumno,Genero, AreaCursos, Cursos
# Register your models here.
admin.site.register(Genero)
admin.site.register(Alumno)
admin.site.register(AreaCursos)
admin.site.register(Cursos)


