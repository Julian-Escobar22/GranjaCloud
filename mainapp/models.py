from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TipoDocumento(models.Model):
    nombre = models.CharField(max_length=150, verbose_name='Nombre')
    descripcion = models.CharField(max_length=250, verbose_name='Descripcion', blank=True, null=True)
    creado = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    actualizado = models.DateTimeField(auto_now=True, verbose_name='Actualizado')
    
    class Meta:
        verbose_name = 'Tipo de documento'
        verbose_name_plural = 'Tipos de documentos'
    
    def __str__(self):
        return self.nombre
    
class Personas(models.Model):
    tipoDocumento = models.ForeignKey(TipoDocumento, verbose_name="Tipo de documento", blank=True, on_delete=models.CASCADE, null=True)
    cedula = models.CharField(max_length=150, verbose_name='Cedula')
    user = models.OneToOneField(User, verbose_name="Usuario", blank=True, on_delete=models.CASCADE, null=True )
    imagen = models.ImageField(default='null', verbose_name="Imagen", upload_to="usuarios", null=True, blank=True)
    publico = models.BooleanField(verbose_name="Publicado?")
    fNacimiento = models.DateField(null=True, blank=True, verbose_name="Fecha de Cumpleaños")
    creado = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    actualizado = models.DateTimeField(auto_now=True, verbose_name='Actualizado')
    
    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
    
    def __str__(self):
        return self.cedula