from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import *
import MySQLdb
from django.db.models import Q
# Create your views here.

idtemporal = 0
host = 'localhost'
db_name = 'Banca'
user = 'root'
contra = 'Marvinkata'
puerto = 3306


def login(request):
    consulta = Administrador.objects.filter(nombre="admin").values_list()
    form = Login()
    variables = {
        "form": form,
    }
    if request.method == 'POST':
        form = Login(data=request.POST)
        datos = form.data
        name = datos.get("nombre")
        passw = datos.get("contra")
        if name == str(consulta[0][0]) and passw == str(consulta[0][1]):
            return render(request,'adminoperaciones.html')
    return render(request, 'adminlogin.html', variables)

def adminoperaciones(request):
    return render(request,'adminoperaciones.html')

def adminCrearCliente(request):
    form = CrearClienteIndividual()
    mensaje = ''
    variable={
        "form": form,
        "mensaje": mensaje,
    }
    if request.method == "POST":
        form = CrearClienteIndividual(data=request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            cui = datos.get("cui")
            nit = datos.get("nit")
            nombres = datos.get("nombres")
            apellidos = datos.get("apellidos")
            fechanacimiento = datos.get("fechanacimiento")
            db = MySQLdb.connect(host=host, user=user, password=contra, db=db_name, connect_timeout=5)
            c = db.cursor()
            consulta = "INSERT INTO USUARIOINDIVIDUAL(cui,nit,nombres,apellidos,fechanacimiento) VALUES(" + str(cui) +","+str(nit)+",'" +nombres+"','"+apellidos+"','"+str(fechanacimiento)+ "')"
            consulta1 = "INSERT INTO USUARIO(contra,cui) VALUES("+str(cui)+","+str(cui)+")"
            c.execute(consulta)
            c.execute(consulta1)
            db.commit()
            c.close()
            form = CrearClienteIndividual()
            z = Usuario.objects.filter(cui=str(cui)).values_list()
            print(z)
            mensaje = "SU USUARIO ES:----> "+str(z[0][0])+"  Y SU CONTRASEÑA ES-----> "+str(cui)
            variable = {
                "form": form,
                "mensaje": mensaje,
            }

        else:
            form = CrearClienteIndividual()
            mensaje = "Ingrese datos"
            variable = {
                "form": form,
                "mensaje": mensaje,
            }
    return render(request, 'adminCrearCliente.html', variable)


def Crearclienteemp(request):
    form = CrearClienteEmpresarial()
    mensaje = "Ingrese datos"
    variable = {
        "mensaje": mensaje,
        "form1": form
    }
    if request.method == "POST":
        form1 = CrearClienteEmpresarial(data=request.POST)
        if form1.is_valid():
            datos = form1.cleaned_data
            #("tipoempresa","nombre","nombrecomercial","nombresrepresentante","apellidosrepresentante")
            tipoempresa = datos.get("tipoempresa")
            nombre = datos.get("nombre")
            nombrecomercial = datos.get("nombrecomercial")
            nombresrepresentante = datos.get("nombresrepresentante")
            apellidosrepresentante = datos.get("apellidosrepresentante")
            db = MySQLdb.connect(host=host, user=user, password=contra, db=db_name, connect_timeout=5)
            c = db.cursor()
            consulta2 ="INSERT INTO USUARIOEMPRESARIAL(tipoempresa,nombre,nombrecomercial,nombresrepresentante,apellidosrepresentante) VALUES('"+datos.get("tipoempresa")+"','"+datos.get("nombre")+ "','" +datos.get("nombrecomercial")+ "','" +datos.get("nombresrepresentante") + "','" +datos.get("apellidosrepresentante")+ "')"
            c.execute(consulta2)
            db.commit()
            c.close()
            zx = Usuarioempresarial.objects.filter(nombrecomercial=nombrecomercial).filter(nombresrepresentante=nombresrepresentante).values_list()
            cd = db.cursor()
            idusemp = str(zx[0][0])
            temporal = idusemp
            print(zx)
            consulta3 = "INSERT INTO USUARIO(contra,idUsuarioemp) VALUES('" +nombrecomercial+ "'," + idusemp + ")"
            cd.execute(consulta3)
            db.commit()
            cd.close()
            print(temporal)
            form1 = CrearClienteEmpresarial()
            zd = Usuario.objects.filter(idusuarioemp=temporal).values_list()
            print(zd)
            mensaje = "SU USUARIO ES:----> " + str(zd[0][0]) + "  Y SU CONTRASEÑA ES-----> " + nombrecomercial
            variable = {
                "mensaje": mensaje,
                "form1": form1
            }
        else:
            print('dader')
    return render(request,'adminCrearClienteemp.html',variable)

def intermedia(request):
    db = MySQLdb.connect(host=host, user=user, password=contra, db=db_name, connect_timeout=30)
    c = db.cursor()

    if request.method == 'POST':
        idUsuario = request.POST['idUsuario']
        diccionario = {}
        diccionario.update(idUsuario = idUsuario)
        variableSesion = request.session['dato'] = diccionario
        marca = request.POST['marca']
        consult = Usuario.objects.filter(idusuario=idUsuario).values_list()
        if consult[0][5] < 3:
            contador = consult[0][5]+1
            consulta = "insert into TARJETADECREDITO(idUsuario,marca) values("+idUsuario+",'"+marca+"')"
            c.execute(consulta)
            update  = "update USUARIO set cantidadtarjetas="+str(contador)+" where idUsuario ="+idUsuario
            c.execute(update)
            db.commit()
            if marca == 'puntos':
                return redirect('prueba')
            elif marca == 'cashback':
                return render(request,'creartarjetacashback.html')
        elif consult[0][5] > 2:
            c.execute("select idUsuario from usuario")
            list = []
            for a in c:
                list.append(a[0])
            return render(request, 'adminintermedia.html', {'list': list})
    else:
        c.execute("select idUsuario from usuario")
        list = []
        for a in c:
            list.append(a[0])
        return render(request, 'adminintermedia.html', {'list': list})

def crearpuntos(request):
    diccionario = request.session['dato']
    usuario = diccionario.get('idUsuario')
    db = MySQLdb.connect(host=host, user=user, password=contra, db=db_name, connect_timeout=30)
    c = db.cursor()
    if request.method == 'POST':
        print('holasers')
    return render(request,'creartarjetapuntos.html',{'mensaje': 'hola'})

def crearcashback(request):
    return render(request,'creartarjetacashback.html')
