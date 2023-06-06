from django.db import models

# Create your models here.


class Genero(models.Model):
    id_genero  = models.AutoField(db_column='idGenero', primary_key=True) 
    genero     = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return str(self.genero)


class Alumno(models.Model):
    rut              = models.CharField(primary_key=True, max_length=10)
    nombre           = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=20)
    apellido_materno = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField(blank=False, null=False) 
    id_genero        = models.ForeignKey('Genero',on_delete=models.CASCADE, db_column='idGenero')  
    telefono         = models.CharField(max_length=45)
    email            = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    direccion        = models.CharField(max_length=50, blank=True, null=True)  
    activo           = models.IntegerField()
  
    def __str__(self):
        return str(self.nombre)+" "+str(self.apellido_paterno)

    class Meta:      
        ordering = ['rut']



# Tarea en Clases

class AreaCursos(models.Model):
    id_Area         = models.AutoField(db_column='idArea', primary_key=True) 
    Descripcion     = models.CharField(max_length=30, blank=False, null=False)

    def __str__(self):
        return str(self.Descripcion)


class ModalCursos(models.Model):
    id_Modal        = models.AutoField(db_column='idModal', primary_key=True) 
    Descripcion     = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return str(self.Descripcion)


class Cursos(models.Model):
    nombre           = models.CharField(max_length=50)
    sence            = models.CharField(max_length=10)
    fecha_creacion   = models.DateField(blank=False, null=False) 
    id_Area          = models.ForeignKey('AreaCursos',on_delete=models.CASCADE, db_column='idArea')  
 #   id_Modal         = models.ForeignKey('ModalCursos',on_delete=models.CASCADE, db_column='idModal')
    modalidad        = models.CharField(max_length=30, blank=True, null=True)
    objetivo         = models.CharField(max_length=200, blank=True, null=True)
    horas            = models.IntegerField()  
    activo           = models.IntegerField()
    img              = models.ImageField(upload_to='img/', null=True, blank=True )
    

    def __str__(self):
        return str(self.nombre)
    class Meta:      
        ordering = ['nombre']

