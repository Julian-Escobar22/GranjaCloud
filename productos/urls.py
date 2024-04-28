from django.urls import path
from .views import * 

urlpatterns = [
    path('v1/pro', Producto_APIView.as_view()),
    path('v1/cat', CategoriaProducto_APIView.as_view()),
    path('v1/cat/<int:pk>', CategoriaProducto_APIView_Detail.as_view()),
]