# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Banco(models.Model):
    id = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'BANCO'


class Cliente(models.Model):
    rut = models.IntegerField(primary_key=True)
    dv = models.CharField(max_length=1)
    nombres = models.CharField(max_length=45)
    apellidos = models.CharField(max_length=45)
    email = models.CharField(max_length=40)
    contrasena = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'CLIENTE'


    def __str__(self):
        rutdv = self.rut.__str__()+"-"+self.dv
        return rutdv, self.nombres

class Comuna(models.Model):
    id = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'COMUNA'


class Contrato(models.Model):
    num_contrato = models.IntegerField(primary_key=True)
    direccion = models.CharField(max_length=45)
    fecha_creacion = models.DateField()
    fecha_termino = models.DateField(blank=True, null=True)
    cliente_rut = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='CLIENTE_rut')  # Field name made lowercase.
    comuna = models.ForeignKey(Comuna, models.DO_NOTHING, db_column='COMUNA_id')  # Field name made lowercase.


    class Meta:
        managed = False
        db_table = 'CONTRATO'
        unique_together = (('num_contrato', 'cliente_rut', 'comuna'),)


class Estacionamiento(models.Model):
    numero = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=45)
    zona = models.ForeignKey('Zona', models.DO_NOTHING, db_column='ZONA_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ESTACIONAMIENTO'
        unique_together = (('numero', 'zona'),)


class Gps(models.Model):
    id = models.IntegerField(primary_key=True)
    lalitud = models.CharField(max_length=45)
    longitud = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'GPS'


class ReporteUso(models.Model):
    nro_reporte = models.IntegerField(primary_key=True)
    fecha = models.DateField()
    cliente_rut = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='CLIENTE_rut')  # Field name made lowercase.
    bicicleta = models.ForeignKey('Bicicleta', models.DO_NOTHING)
    gps = models.ForeignKey(Gps, models.DO_NOTHING, db_column='GPS_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'REPORTE_USO'
        unique_together = (('nro_reporte', 'cliente_rut', 'bicicleta', 'gps'),)


class TarjetaCredito(models.Model):
    numero = models.IntegerField(primary_key=True)
    verificado = models.IntegerField()
    fecha_vencimiento = models.DateField()
    banco = models.ForeignKey(Banco, models.DO_NOTHING, db_column='BANCO_id')  # Field name made lowercase.
    cliente_rut = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='CLIENTE_rut')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TARJETA_CREDITO'
        unique_together = (('numero', 'banco', 'cliente_rut'),)


class TarjetaMuni(models.Model):
    numero = models.IntegerField(primary_key=True)
    estado = models.IntegerField()
    cliente_rut = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='CLIENTE_rut')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TARJETA_MUNI'
        unique_together = (('numero', 'cliente_rut'),)


class Zona(models.Model):
    id = models.IntegerField(primary_key=True)
    direccion = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'ZONA'


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
    first_name = models.CharField(max_length=30)
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


class Bicicleta(models.Model):
    id = models.IntegerField(primary_key=True)
    estacionamiento_numero = models.ForeignKey(Estacionamiento, models.DO_NOTHING, db_column='ESTACIONAMIENTO_numero',related_name='estacionamiento_numero')  # Field name made lowercase.
    estacionamiento_zona = models.ForeignKey(Estacionamiento, models.DO_NOTHING, db_column='ESTACIONAMIENTO_ZONA_id',related_name='estacionamiento_zona')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bicicleta'
        unique_together = (('id', 'estacionamiento_numero', 'estacionamiento_zona'),)


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
