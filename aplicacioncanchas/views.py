from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.http import HttpResponse
from .models import *
from django.contrib import messages
from datetime import date
from .forms import RegistroUsuarioForm


# Página de inicio luego del login (opcional)
def inicio(request):
    if 'usuario_id' not in request.session:
        return redirect('login')
    return render(request, 'inicio.html')


# 1. Login de usuario
def login_view(request):
    if request.method == 'POST':
        correo = request.POST.get('correo')
        contrasena = request.POST.get('contrasena')
        try:
            usuario = Usuario.objects.get(correo=correo, contrasena=contrasena)
            request.session['usuario_id'] = usuario.id_usuario
            return redirect('reservar')  # Redirige a la página de reservas
        except Usuario.DoesNotExist:
            messages.error(request, 'Credenciales inválidas')
    return render(request, 'login.html')


# 2. Reservar cancha con servicios adicionales
def reservar_cancha(request):
    if 'usuario_id' not in request.session:
        return redirect('login')

    if request.method == 'POST':
        id_usuario = request.session.get('usuario_id')
        id_cancha = request.POST['cancha_id']
        id_horario = request.POST['horario_id']
        fecha = request.POST['fecha']
        observaciones = request.POST.get('observaciones', '')

        reserva = Reserva.objects.create(
            id_usuario=id_usuario,
            id_cancha=id_cancha,
            id_horario=id_horario,
            id_estado=1,  # Estado pendiente
            fecha_reserva=fecha,
            observaciones=observaciones,
            id_empleado=None
        )

        servicios = request.POST.getlist('servicios')
        for servicio_id in servicios:
            ReservaServicio.objects.create(id_reserva=reserva.id_reserva, id_servicio=servicio_id)

        return redirect('mis_reservas')

    canchas = Cancha.objects.all()
    horarios = Horario.objects.all()
    servicios = ServicioAdicional.objects.all()
    return render(request, 'reservar.html', {'canchas': canchas, 'horarios': horarios, 'servicios': servicios})


# 3. Ver reservas realizadas por el usuario
def mis_reservas(request):
    if 'usuario_id' not in request.session:
        return redirect('login')

    id_usuario = request.session.get('usuario_id')
    reservas = Reserva.objects.filter(id_usuario=id_usuario)
    return render(request, 'mis_reservas.html', {'reservas': reservas})


# 4. Agregar comentario a una cancha
def agregar_comentario(request, id_cancha):
    if 'usuario_id' not in request.session:
        return redirect('login')

    if request.method == 'POST':
        Comentario.objects.create(
            id_usuario=request.session.get('usuario_id'),
            id_cancha=id_cancha,
            texto=request.POST['texto'],
            fecha_comentario=date.today()
        )
        return redirect('mis_reservas')
    return render(request, 'comentario.html', {'id_cancha': id_cancha})


# 5. Procesar pago de una reserva
def pagar_reserva(request, id_reserva):
    if 'usuario_id' not in request.session:
        return redirect('login')

    if request.method == 'POST':
        Pago.objects.create(
            id_reserva=id_reserva,
            id_metodo_pago=request.POST['metodo_pago'],
            monto=request.POST['monto'],
            fecha_pago=date.today()
        )
        return redirect('mis_reservas')
    metodos = MetodoPago.objects.all()
    return render(request, 'pagar.html', {'id_reserva': id_reserva, 'metodos': metodos})


# 6. Panel administrativo básico para empleados
def panel_admin(request):
    if 'usuario_id' not in request.session:
        return redirect('login')

    usuario_id = request.session.get('usuario_id')
    empleado = Empleado.objects.filter(id_empleado=usuario_id).first()
    if not empleado:
        return HttpResponse('Acceso denegado')

    reservas = Reserva.objects.all()
    return render(request, 'admin_panel.html', {'reservas': reservas})


# 7. Logout
def logout_view(request):
    logout(request)  # Borra también las variables de sesión si usas auth, pero por seguridad...
    request.session.flush()  # ✅ Borra toda la sesión
    return redirect('login')


# 8. Registro de usuario
def registrar_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registro exitoso, por favor inicia sesión.")
            return redirect('login')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'registro.html', {'form': form})
