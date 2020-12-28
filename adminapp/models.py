# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Administrador(models.Model):
    nombre = models.CharField(db_column='Nombre', primary_key=True, max_length=15)  # Field name made lowercase.
    contra = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'administrador'


class Cuenta(models.Model):
    numerocuenta = models.AutoField(primary_key=True)
    idusuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='idUsuario', blank=True, null=True)  # Field name made lowercase.
    tipomoneda = models.CharField(max_length=1, blank=True, null=True)
    estaactiva = models.CharField(db_column='estaActiva', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tipocuenta = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cuenta'


class Cuentaahorro(models.Model):
    numerocuenta = models.OneToOneField(Cuenta, models.DO_NOTHING, db_column='numerocuenta', primary_key=True)
    interes = models.IntegerField(blank=True, null=True)
    saldo = models.DecimalField(max_digits=35, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cuentaahorro'


class Cuentamonetaria(models.Model):
    numerocuenta = models.OneToOneField(Cuenta, models.DO_NOTHING, db_column='numerocuenta', primary_key=True)
    preautoriza = models.CharField(max_length=2, blank=True, null=True)
    nocheques = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cuentamonetaria'


class Cuentapf(models.Model):
    numerocuenta = models.OneToOneField(Cuenta, models.DO_NOTHING, db_column='numerocuenta', primary_key=True)
    interes = models.IntegerField(blank=True, null=True)
    saldo = models.DecimalField(max_digits=35, decimal_places=3, blank=True, null=True)
    tiempo = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cuentapf'


class Tarjetadecashback(models.Model):
    numerotarjeta = models.OneToOneField('Tarjetadecredito', models.DO_NOTHING, db_column='numerotarjeta', primary_key=True)
    limite = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    cashback = models.DecimalField(max_digits=35, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tarjetadecashback'


class Tarjetadecredito(models.Model):
    numerotarjeta = models.AutoField(primary_key=True)
    idusuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='idUsuario', blank=True, null=True)  # Field name made lowercase.
    marca = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tarjetadecredito'


class Tarjetadepuntos(models.Model):
    numerotarjeta = models.OneToOneField(Tarjetadecredito, models.DO_NOTHING, db_column='numerotarjeta', primary_key=True)
    limite = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    puntos = models.DecimalField(max_digits=35, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tarjetadepuntos'


class Usuario(models.Model):
    idusuario = models.AutoField(db_column='idUsuario', primary_key=True)  # Field name made lowercase.
    contra = models.CharField(max_length=20, blank=True, null=True)
    cui = models.ForeignKey('Usuarioindividual', models.DO_NOTHING, db_column='CUI', blank=True, null=True)  # Field name made lowercase.
    idusuarioemp = models.ForeignKey('Usuarioempresarial', models.DO_NOTHING, db_column='idUsuarioemp', blank=True, null=True)  # Field name made lowercase.
    deuda = models.DecimalField(max_digits=65, decimal_places=3, blank=True, null=True)
    cantidadtarjetas = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuario'


class Usuarioempresarial(models.Model):
    idusuarioemp = models.AutoField(db_column='idUsuarioemp', primary_key=True)  # Field name made lowercase.
    tipoempresa = models.CharField(db_column='tipoEmpresa', max_length=18, blank=True, null=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=40, blank=True, null=True)
    nombrecomercial = models.CharField(db_column='nombreComercial', max_length=40, blank=True, null=True)  # Field name made lowercase.
    nombresrepresentante = models.CharField(db_column='nombresRepresentante', max_length=35, blank=True, null=True)  # Field name made lowercase.
    apellidosrepresentante = models.CharField(db_column='apellidosRepresentante', max_length=35, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'usuarioempresarial'


class Usuarioindividual(models.Model):
    cui = models.BigIntegerField(db_column='CUI', primary_key=True)  # Field name made lowercase.
    nit = models.IntegerField(db_column='NIT', blank=True, null=True)  # Field name made lowercase.
    nombres = models.CharField(max_length=30, blank=True, null=True)
    apellidos = models.CharField(max_length=30, blank=True, null=True)
    fechanacimiento = models.DateField(db_column='fechaNacimiento', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'usuarioindividual'
