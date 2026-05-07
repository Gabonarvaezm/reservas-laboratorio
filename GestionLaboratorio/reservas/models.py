from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class Reserva(models.Model):

    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('aprobada', 'Aprobada'),
        ('rechazada', 'Rechazada'),
    ]

    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    laboratorio = models.CharField(
        max_length=100
    )

    fecha = models.DateField()

    hora_inicio = models.TimeField()

    hora_fin = models.TimeField()

    estado = models.CharField(
        max_length=20,
        choices=ESTADOS,
        default='pendiente'
    )

    motivo = models.TextField()

    fecha_creacion = models.DateTimeField(
        auto_now_add=True
    )

    def clean(self):

        conflicto = Reserva.objects.filter(
            laboratorio=self.laboratorio,
            fecha=self.fecha,
            hora_inicio__lt=self.hora_fin,
            hora_fin__gt=self.hora_inicio
        ).exclude(id=self.id)

        if conflicto.exists():

            raise ValidationError(
                "Ya existe una reserva en ese horario."
            )

    def __str__(self):

        return f"{self.laboratorio} - {self.fecha}"