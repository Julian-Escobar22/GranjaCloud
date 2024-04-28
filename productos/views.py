from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ProductoSerializers, CategoriaProductoSerializers
from .models import Producto, CategoriaProducto
from rest_framework import status
from django.http import Http404

# Create your views here.

class Producto_APIView(APIView):
    
    def post(self, request, format=None):
        serializer = ProductoSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoriaProducto_APIView(APIView):
    
    def post(self, request, format=None):
        serializer = CategoriaProductoSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
class CategoriaProducto_APIView_Detail(APIView):
    
    def get_object(self, pk):
        try:
            return CategoriaProducto.objects.get(pk=pk)
        except CategoriaProducto.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        categoriaProducto = self.get_object(pk)
        serializer = CategoriaProductoSerializers(categoriaProducto)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        categoriaProducto = self.get_object(pk)
        serializer = CategoriaProductoSerializers(categoriaProducto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_410_GONE)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    def delete(self, request, pk, format=None):
        categoriaProducto = self.get_object(pk)
        categoriaProducto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)