from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
    path('adminlogin/',views.login),
    path('adminoperaciones/',views.adminoperaciones),
    path('adminCrearCliente/',views.adminCrearCliente),
    path('Crearclienteemp/',views.Crearclienteemp),
    path('CrearMonetaria/',views.crearMonetaria),
    path('CrearAhorro/',views.crearAhorro),
    path('CrearPF/',views.crearPF),
    path('intermedia/',views.intermedia1),
]
