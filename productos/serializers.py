from rest_framework import serializers
from .models import CategoriaProducto, Producto

class CategoriaProductoSerializers(serializers.ModelSerializer):
    class Meta:
        model = CategoriaProducto
        fields = '__all__'

class ProductoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'