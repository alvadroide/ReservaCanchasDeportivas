from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),                     # ← ahora esta es la página principal
    path('login/', views.login_view, name='login'),            # ← login va a /login
    path('logout/', views.logout_view, name='logout'),
    path('reservar/', views.reservar_cancha, name='reservar'),
    path('mis_reservas/', views.mis_reservas, name='mis_reservas'),
    path('comentario/<int:id_cancha>/', views.agregar_comentario, name='comentario'),
    path('pagar/<int:id_reserva>/', views.pagar_reserva, name='pagar'),
    path('admin_panel/', views.panel_admin, name='admin_panel'),
    path('registrarse/', views.registrar_usuario, name='registrarse'),
]
