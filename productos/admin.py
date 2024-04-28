from django.contrib import admin
from .models import CategoriaProducto, Producto

# Register your models here.
class CategoriaProductoAdmin(admin.ModelAdmin):
    readonly_fields = ('creado', 'actualizado')
    search_fields = ('nombre', )
    list_display=('nombre', 'creado', 'actualizado' )
    ordering = ('-creado',)
    
class ProductoAdmin(admin.ModelAdmin):
    readonly_fields = ('creado', 'actualizado')
    search_fields = ('nombre', 'cantidad', 'precio')
    list_filter = ('publico','fLote')
    list_display=('nombre', 'cantidad', 'precio', 'creado', 'actualizado' )
    ordering = ('-creado',)

    
admin.site.register(CategoriaProducto, CategoriaProductoAdmin)
admin.site.register(Producto, ProductoAdmin)