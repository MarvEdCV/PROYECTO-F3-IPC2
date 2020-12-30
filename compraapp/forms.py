from django import forms
from adminapp.models import *

class comprass(forms.ModelForm):
    class Meta:
        model = Compratarjeta
        fields =("fechacompra","descripcion","monto")