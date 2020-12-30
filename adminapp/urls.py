from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
    path('adminlogin/',views.login),
    path('adminoperaciones/',views.adminoperaciones),
    path('adminCrearCliente/',views.adminCrearCliente),
    path('Crearclienteemp/',views.Crearclienteemp),
    path('intermedia/',views.intermedia),
    path('tarjetapuntos/',views.crearpuntos,name='prueba'),
    path('tarjetacashback/',views.crearcashback,name='cashback'),
]
