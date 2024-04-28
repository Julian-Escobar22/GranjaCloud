from django.db import models

# Create your models here.
class CategoriaProducto(models.Model):
    nombre = models.CharField(max_length=150, verbose_name='Nombre')
    descripcion = models.CharField(max_length=250, verbose_name='Descripcion', blank=True, null=True)
    creado = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    actualizado = models.DateTimeField(auto_now=True, verbose_name='Actualizado')
    
    class Meta:
        verbose_name = 'Categoria Producto'
        verbose_name_plural = 'Categorias Productos'
    
    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    categoria = models.ForeignKey(CategoriaProducto, verbose_name="Categoria", blank=True, on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=250, verbose_name='Nombre')
    cantidad = models.CharField(max_length=150, verbose_name='Cantidad')
    precio = models.CharField(max_length=150, verbose_name='Costo')
    descripcion = models.TextField(verbose_name='Descripcion', blank=True, null=True)
    imagen = models.ImageField(default='null', verbose_name="Imagen", upload_to="productos", null=True, blank=True)
    publico = models.BooleanField(verbose_name="Publicado?")
    fLote = models.DateField(null=True, blank=True, verbose_name="Fecha de Lote")
    creado = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    actualizado = models.DateTimeField(auto_now=True, verbose_name='Actualizado')
    
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
    
    def __str__(self):
        return self.nombre