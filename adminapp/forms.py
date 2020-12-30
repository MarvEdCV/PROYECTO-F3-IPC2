from django import forms
from adminapp.models import *

class Login(forms.ModelForm):
    class Meta:
        model = Administrador
        fields =("nombre","contra")

class CrearClienteIndividual(forms.ModelForm):
    class Meta:
        model = Usuarioindividual
        fields = ("cui","nit","nombres","apellidos","fechanacimiento")

class CrearClienteEmpresarial(forms.ModelForm):
    class Meta:
        model = Usuarioempresarial
        fields = ("tipoempresa","nombre","nombrecomercial","nombresrepresentante","apellidosrepresentante")

class creartarjetapuntos(forms.ModelForm):
    class Meta:
        model = Tarjetadepuntos
        fields =("limite","puntos")

class creartarjetacashback(forms.ModelForm):
    class Meta:
        model = Tarjetadecashback
        fields =("limite","cashback")

