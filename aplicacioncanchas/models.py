from django.db import models

class ReservaServicio(models.Model):
    id_reserva = models.IntegerField()
    id_servicio = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Reserva_Servicio'


class EstadoReserva(models.Model):
    id_estado = models.IntegerField(primary_key=True)
    nombre_estado = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'Estado_Reserva'


class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    rut = models.CharField(max_length=20)
    correo = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    contrasena = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'Usuario'


class RolEmpleado(models.Model):
    id_rol = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'Rol_Empleado'


class Reserva(models.Model):
    id_reserva = models.AutoField(primary_key=True)
    id_usuario = models.IntegerField()
    id_cancha = models.IntegerField()
    id_horario = models.IntegerField()
    id_estado = models.IntegerField()
    fecha_reserva = models.DateField()
    observaciones = models.TextField(blank=True, null=True)
    id_empleado = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Reserva'


class Empleado(models.Model):
    id_empleado = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)
    rol = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'Empleado'


class Cancha(models.Model):
    id_cancha = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    id_deporte = models.IntegerField()
    techada = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'Cancha'


class Horario(models.Model):
    id_horario = models.AutoField(primary_key=True)
    hora_inicio = models.TimeField()
    hora_termino = models.TimeField()

    class Meta:
        managed = False
        db_table = 'Horario'


class Deporte(models.Model):
    id_deporte = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'Deporte'


class MetodoPago(models.Model):
    id_metodo_pago = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'Metodo_pago'


class Pago(models.Model):
    id_pago = models.AutoField(primary_key=True)
    id_reserva = models.IntegerField()
    id_metodo_pago = models.IntegerField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pago = models.DateField()

    class Meta:
        managed = False
        db_table = 'Pago'


class Comentario(models.Model):
    id_comentario = models.AutoField(primary_key=True)
    id_usuario = models.IntegerField()
    id_cancha = models.IntegerField()
    texto = models.TextField()
    fecha_comentario = models.DateField()

    class Meta:
        managed = False
        db_table = 'Comentarios'

class ServicioAdicional(models.Model):
    id_servicio = models.IntegerField(primary_key=True)
    descripcion = models.TextField()
    precio = models.IntegerField()

    class Meta:
        db_table = "Servicio_Adicional"
        managed = False