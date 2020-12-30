from django.shortcuts import render, redirect
from .forms import *
import MySQLdb
# Create your views here.
idtemporal = 0
host = 'localhost'
db_name = 'Banca'
user = 'root'
contra = 'Marvinkata'
puerto = 3306

def login(request):
    db = MySQLdb.connect(host=host, user=user, password=contra, db=db_name, connect_timeout=30)
    c = db.cursor()
    list = []
    var={
        'list':list
    }
    if request.method == 'POST':
        idUsuario = request.POST['idUsuario']
        diccionario = {}
        diccionario.update(idUsuario=idUsuario)
        variableSesion = request.session['dato'] = diccionario
        return redirect('ope')
    else:
        c.execute("select idUsuario from usuario")
        list = []
        for a in c:
            list.append(a[0])
        var = {
            'list': list
        }
        return render(request, 'login.html',var)

def operaciones(request):
    return render(request,'Operaciones.html')
def trcuentapropia(request):
    return render(request,'trcuentaspropias.html')

def trcuentaterceros(request):
    return render(request,'trcuentasterceros.html')
def preautorizacion(request):
    return render(request,'preautorizacion.html')
def pagoplanilla(request):
    return render(request,'pagoplanilla.html')
def servicios(request):
    return render(request,'sevicios.html')
def solicitarprestamo(request):
    return render(request,'solicitarprestamo.html')
def agregarterceros(request):
    return render(request,'agregarterceros.html')
def suspendercuenta(request):
    return render(request,'suspendercuenta.html')
def activarcuenta(request):
    return render(request,'activarcuenta.html')
def estadodecuenta(request):
    return render(request,'estadodecuenta.html')