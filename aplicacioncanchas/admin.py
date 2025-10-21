from django.contrib import admin
from .models import (
    Deporte,
    EstadoReserva,
    MetodoPago,
    ServicioAdicional,
    Usuario,
    RolEmpleado,
    Cancha,
    Comentario,
    Horario,
    Reserva,
    ReservaServicio,
    Pago,
)

admin.site.register(Deporte)
admin.site.register(EstadoReserva)
admin.site.register(MetodoPago)
admin.site.register(ServicioAdicional)
admin.site.register(Usuario)
admin.site.register(RolEmpleado)
admin.site.register(Cancha)
admin.site.register(Comentario)
admin.site.register(Horario)
admin.site.register(Reserva)
admin.site.register(ReservaServicio)
admin.site.register(Pago)
