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
# Create your views here.
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
        return redirect('compra')
    else:
        c.execute("select idUsuario from usuario")
        list = []
        for a in c:
            list.append(a[0])
        var = {
            'list': list
        }
        return render(request, 'compralogin.html',var)
def compra(request):
    return render(request,'compra.html')