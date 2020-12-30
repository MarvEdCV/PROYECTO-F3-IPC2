from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
    path('compralogin/',views.login),
    path('compra/',views.compra,name='compra'),
]
