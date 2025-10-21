from django import forms
from .models import Usuario

class RegistroUsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'rut', 'correo', 'telefono', 'contrasena']
        widgets = {
            'contrasena': forms.PasswordInput(),
        }
