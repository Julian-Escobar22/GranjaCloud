from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('inicio/', views.index, name='inicio'),  # Cambiado a 'inicio/' para distinguir de la vista de inicio de sesión
    path('iniciar_sesion/', views.iniciar_sesion, name='iniciar_sesion'),  # URL para el inicio de sesión
    path('registro/', views.registro, name='registro'),  # URL para el registro de usuarios
]
