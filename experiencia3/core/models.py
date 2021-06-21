from django.db import models

# Create your models here.
class Especialidad(models.Model):

    idEspecialidad = models.IntegerField(primary_key=True, verbose_name='Id de la especialidad')

    nombreEspecialidad = models.CharField(max_length=50, verbose_name='Nombre de la especialidad')



    def __str__(self):

        return self.nombreEspecialidad

class Personas(models.Model):

    nombre = models.CharField(max_length=40, primary_key=True, verbose_name='Nombre')

    edad = models.CharField(max_length=2, verbose_name='Edad')

    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)

    descrip = models.TextField(max_length=150, verbose_name='Descripción especialidad', default='')

    image = models.ImageField(upload_to='images/', null=True, blank=True)




    def __str__(self):

        return self.nombre

class Reseña(models.Model):
    idReseña=models.IntegerField(primary_key=True, verbose_name='Id de la reseña')
    numeroEstrellas=models.CharField(max_length=1, verbose_name='Numero estrellas')

    def __str__(self):

        return self.numeroEstrellas

class Input(models.Model):

    nombreUsuario = models.CharField(max_length=40, primary_key=True, verbose_name='Nombre Completo')

    edad= models.CharField(max_length=2, verbose_name='Edad')

    correoElectronico= models.CharField(max_length=40, verbose_name='Correo Electrónico')

    personalContratado= models.CharField(max_length=40, verbose_name='Nombre del Personal')

    numeroEstrellas = models.ForeignKey(Reseña, on_delete=models.CASCADE)

    comentario=models.TextField(max_length=200,  verbose_name='Comentario')



    def __str__(self):

        return self.nombreUsuario