from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Reserva


class RegistroDocenteForm(UserCreationForm):

    first_name = forms.CharField(
        max_length=100,
        required=True
    )

    last_name = forms.CharField(
        max_length=100,
        required=True
    )

    email = forms.EmailField(
        required=True
    )

    class Meta:

        model = User

        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        ]


class RegistroAdministradorForm(UserCreationForm):

    first_name = forms.CharField(
        max_length=100,
        required=True
    )

    last_name = forms.CharField(
        max_length=100,
        required=True
    )

    email = forms.EmailField(
        required=True
    )

    class Meta:

        model = User

        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        ]


class ReservaForm(forms.ModelForm):

    class Meta:

        model = Reserva

        fields = [
            'laboratorio',
            'fecha',
            'hora_inicio',
            'hora_fin',
            'motivo'
        ]

        widgets = {

            'fecha': forms.DateInput(
                attrs={
                    'type': 'date'
                }
            ),

            'hora_inicio': forms.TimeInput(
                attrs={
                    'type': 'time'
                }
            ),

            'hora_fin': forms.TimeInput(
                attrs={
                    'type': 'time'
                }
            ),

            'motivo': forms.Textarea(
                attrs={
                    'rows': 4
                }
            )
        }

    def clean(self):

        cleaned_data = super().clean()

        hora_inicio = cleaned_data.get(
            'hora_inicio'
        )

        hora_fin = cleaned_data.get(
            'hora_fin'
        )

        if hora_inicio and hora_fin:

            if hora_inicio >= hora_fin:

                raise forms.ValidationError(
                    'La hora final debe ser mayor.'
                )

        return cleaned_data