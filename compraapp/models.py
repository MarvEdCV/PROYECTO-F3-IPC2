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


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Compratarjeta(models.Model):
    id_compra = models.AutoField(primary_key=True)
    fechacompra = models.DateField(blank=True, null=True)
    idusuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='idUsuario', blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(max_length=60, blank=True, null=True)
    monto = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    numerotarjeta = models.ForeignKey('Tarjetadecredito', models.DO_NOTHING, db_column='numerotarjeta', blank=True, null=True)
    moneda = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'compratarjeta'


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


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Tarjetadecashback(models.Model):
    numerotarjeta = models.OneToOneField('Tarjetadecredito', models.DO_NOTHING, db_column='numerotarjeta', primary_key=True)
    limite = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
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
    limite = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
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
