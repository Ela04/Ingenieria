# Generated by Django 4.2.1 on 2023-06-02 21:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AreaCursos',
            fields=[
                ('id_Area', models.AutoField(db_column='idArea', primary_key=True, serialize=False)),
                ('Descripcion', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id_genero', models.AutoField(db_column='idGenero', primary_key=True, serialize=False)),
                ('genero', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Cursos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('sence', models.CharField(max_length=10)),
                ('fecha_creacion', models.DateField()),
                ('objetivo', models.CharField(blank=True, max_length=200, null=True)),
                ('horas', models.IntegerField()),
                ('activo', models.IntegerField()),
                ('img', models.ImageField(blank=True, null=True, upload_to='img/')),
                ('id_Area', models.ForeignKey(db_column='idArea', on_delete=django.db.models.deletion.CASCADE, to='alumnos.areacursos')),
            ],
            options={
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('rut', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
                ('apellido_paterno', models.CharField(max_length=20)),
                ('apellido_materno', models.CharField(max_length=20)),
                ('fecha_nacimiento', models.DateField()),
                ('telefono', models.CharField(max_length=45)),
                ('email', models.EmailField(blank=True, max_length=100, null=True, unique=True)),
                ('direccion', models.CharField(blank=True, max_length=50, null=True)),
                ('activo', models.IntegerField()),
                ('id_genero', models.ForeignKey(db_column='idGenero', on_delete=django.db.models.deletion.CASCADE, to='alumnos.genero')),
            ],
            options={
                'ordering': ['rut'],
            },
        ),
    ]
