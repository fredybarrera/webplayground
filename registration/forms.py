# Archivo para extender el formulario de registro 'UserCreationForm'

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Requerido, máx 254 carácteres, email válido")

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    # Para valodar la unicidad del campo email
    def clean_email(self):
        email = self.cleaned_data.get('email')
        # Valida si el email ingresado ya existe en la base de datos
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('El correo electrónico ya está registrado, utilizar otro.')
        return email
