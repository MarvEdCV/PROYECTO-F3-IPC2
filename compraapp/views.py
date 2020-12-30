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
    db = MySQLdb.connect(host=host, user=user, password=contra, db=db_name, connect_timeout=30)
    c = db.cursor()
    diccionario = request.session['dato']
    usuario = diccionario.get('idUsuario')
    form = comprass()
    c.execute("select numerotarjeta from tarjetadecredito where idUsuario=" + usuario)
    list = []
    for a in c:
        list.append(a[0])
    var ={
        "form":form
    }
    if request.method == 'POST':
        form = comprass(data=request.POST)
        Notarjeta = request.POST['tareg']
        tipo = Tarjetadecredito.objects.filter(numerotarjeta=Notarjeta).values_list()
        if form.is_valid():
            datos = form.cleaned_data
            fecha = datos.get("fechacompra")
            desc = datos.get("descripcion")
            monto = datos.get("monto")
            if tipo[0][2] == 'puntos':
                a = Tarjetadepuntos.objects.filter(numerotarjeta=Notarjeta).values_list()
                saldo = str(a[0][1])
                if request.POST['moneda'] == 'Q' and a[0][1] > monto:
                    insert = "insert into COMPRATARJETA (fechacompra,idUsuario,descripcion,monto,numerotarjeta,moneda) Values(" \
                             "'"+str(fecha)+"',"+str(usuario)+",'"+desc+"',"+str(monto)+","+str(Notarjeta)+",'Q')"
                    print(insert)

                    nuevolimite = a[0][1] - monto
                    if monto>=0.01 and monto<=100:
                        puntos = float(a[0][2])+(float(monto)*0)
                    if monto>=100.01 and monto<=500:
                        puntos = float(a[0][2])+float(monto)*0.02
                    if monto>=500.01 and monto<=2000:
                        puntos = float(a[0][2])+float(monto)*0.04
                    if monto>=2000.01:
                        puntos=float(a[0][2])+float(monto)*0.05
                    update = "update tarjetadepuntos set limite=" + str(nuevolimite) + ",puntos="+str(puntos) +"where numerotarjeta =" + str(Notarjeta)
                    print(update)
                    c.execute(insert)
                    c.execute(update)
                if request.POST['moneda'] == '$' and (float(a[0][1])/7.63) > monto:
                    insert = "insert into COMPRATARJETA (fechacompra,idUsuario,descripcion,monto,numerotarjeta,moneda) Values(" \
                             "'"+str(fecha)+"',"+str(usuario)+",'"+desc+"',"+str(monto)+","+str(Notarjeta)+",'$')"
                    print(insert)
                    nuevolimite = float(a[0][1]) - float(monto)*7.63
                    if monto >= (0.01/7.63) and monto <= (100/7.63):
                        puntos = float(a[0][2])+(float(monto)*0)
                    if monto>=(100.01/7.63) and monto<= (500/7.63):
                        puntos = float(a[0][2])+float(monto)*0.02*7.63
                    if monto>=(500.01/7.63) and monto<=(2000/7.63):
                        puntos = float(a[0][2])+float(monto)*0.04*7.63
                    if monto>=(2000.01/7.63):
                        puntos=float(a[0][2])+float(monto)*0.05*7.63
                    update = "update tarjetadepuntos set limite=" + str(nuevolimite) + ",puntos="+str(puntos) +"where numerotarjeta =" + str(Notarjeta)
                    print(update)
                    c.execute(insert)
                    c.execute(update)
            if tipo[0][2] == 'cashback':
                a = Tarjetadecashback.objects.filter(numerotarjeta=Notarjeta).values_list()
                saldo = str(a[0][1])
                if request.POST['moneda'] == 'Q' and a[0][1] > monto:
                    insert = "insert into COMPRATARJETA (fechacompra,idUsuario,descripcion,monto,numerotarjeta,moneda) Values(" \
                             "'"+str(fecha)+"',"+str(usuario)+",'"+desc+"',"+str(monto)+","+str(Notarjeta)+",'Q')"
                    print(insert)
                    nuevolimite = a[0][1] - monto
                    if monto>=0.01 and monto<=200:
                        puntos = float(a[0][2])+(float(monto)*0)
                    if monto>=200.01 and monto<=700:
                        puntos = float(a[0][2])+float(monto)*0.02
                    if monto>=700.01:
                        puntos = float(a[0][2])+float(monto)*0.05
                    update = "update tarjetadecashback set limite=" + str(nuevolimite) + ",cashback="+str(puntos) +"where numerotarjeta =" + str(Notarjeta)
                    print(update)
                    c.execute(insert)
                    c.execute(update)
                if request.POST['moneda'] == '$' and (float(a[0][1])/7.87) > monto:
                    inserts = "insert into COMPRATARJETA (fechacompra,idUsuario,descripcion,monto,numerotarjeta,moneda) Values(" \
                             "'"+str(fecha)+"',"+str(usuario)+",'"+desc+"',"+str(monto)+","+str(Notarjeta)+",'$')"
                    #print(insert)
                    nuevolimite = float(a[0][1]) - float(monto)*7.87
                    if monto >= (0.01/7.87) and monto <= (200/7.87):
                        puntos = float(a[0][2])+(float(monto)*0)
                    if monto>=(200.01/7.63) and monto<= (700/7.87):
                        puntos = float(a[0][2])+float(monto)*0.02*7.87
                    if monto>=(700.01/7.87):
                        puntos = float(a[0][2])+float(monto)*0.05*7.87
                    updates = "update tarjetadecashback set limite=" + str(nuevolimite) + ",cashback="+str(puntos) +"where numerotarjeta =" + str(Notarjeta)
                    #print(update)
                    c.execute(inserts)
                    c.execute(updates)
            db.commit()
            form = comprass()
            c.execute("select numerotarjeta from tarjetadecredito where idUsuario=" + usuario)
            list = []
            for a in c:
                list.append(a[0])
            var = {
                'list': list,
                'form': form,
                #'ser': ser,
                #'serd': serd

            }
            return render(request,'compra.html',var)
    else:
        form = comprass()
        c.execute("select numerotarjeta from tarjetadecredito where idUsuario="+usuario)
        list = []
        for a in c:
            list.append(a[0])
        var = {
            'list': list,
            'form':form
        }
        return render(request, 'compra.html', var)


