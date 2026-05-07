from django.contrib.auth.views import LoginView, LogoutView

from django.views.generic import (
    TemplateView,
    CreateView,
    ListView,
    UpdateView,
    DeleteView
)

from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)

from django.contrib.auth.forms import UserCreationForm

from django.urls import reverse_lazy

from django.contrib.auth.models import (
    User,
    Group
)

from django.shortcuts import redirect

from django.http import HttpResponse

import csv

from .models import Reserva




class registro_docente(CreateView):

    model = User

    form_class = UserCreationForm

    template_name = 'registro_docente.html'

    success_url = reverse_lazy('login')

    def form_valid(self, form):

        response = super().form_valid(form)

        grupo = Group.objects.get(
            name='Docentes'
        )

        self.object.groups.add(grupo)

        return response




class registro_administrador(CreateView):

    model = User

    form_class = UserCreationForm

    template_name = 'registro_administrador.html'

    success_url = reverse_lazy('login')

    def form_valid(self, form):

        response = super().form_valid(form)

        grupo = Group.objects.get(
            name='Administradores'
        )

        self.object.groups.add(grupo)

        return response



class login_view(LoginView):

    template_name = 'login.html'




class logout_view(LogoutView):

   next_page = 'login'



class ReservaListView(
    LoginRequiredMixin,
    ListView
):

    model = Reserva

    template_name = 'reservas/lista.html'

    context_object_name = 'reservas'

    def get_queryset(self):

        queryset = Reserva.objects.all()

        fecha = self.request.GET.get('fecha')

        laboratorio = self.request.GET.get(
            'laboratorio'
        )

        if fecha:

            queryset = queryset.filter(
                fecha=fecha
            )

        if laboratorio:

            queryset = queryset.filter(
                laboratorio__icontains=laboratorio
            )

        return queryset



class ReservaCreateView(
    LoginRequiredMixin,
    CreateView
):

    model = Reserva

    fields = [
        'laboratorio',
        'fecha',
        'hora_inicio',
        'hora_fin',
        'motivo'
    ]

    template_name = 'reservas/form.html'

    success_url = reverse_lazy('lista')

    def form_valid(self, form):

        form.instance.usuario = self.request.user

        return super().form_valid(form)




class ReservaUpdateView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    UpdateView
):

    model = Reserva

    fields = [
        'laboratorio',
        'fecha',
        'hora_inicio',
        'hora_fin',
        'motivo'
    ]

    template_name = 'reservas/form.html'

    success_url = reverse_lazy('lista')

    def test_func(self):

        reserva = self.get_object()

        return (
            self.request.user == reserva.usuario
            and reserva.estado == 'pendiente'
        )



class ReservaDeleteView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    DeleteView
):

    model = Reserva

    template_name = 'reservas/eliminar.html'

    success_url = reverse_lazy('lista')

    def test_func(self):

        reserva = self.get_object()

        return (
            self.request.user == reserva.usuario
            and reserva.estado == 'pendiente'
        )



class AprobarReservaView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    UpdateView
):

    model = Reserva

    fields = []

    success_url = reverse_lazy('lista')

    def test_func(self):

        return self.request.user.groups.filter(
            name='Administradores'
        ).exists()

    def post(self, request, *args, **kwargs):

        reserva = self.get_object()

        reserva.estado = 'aprobada'

        reserva.save()

        return redirect('lista')




class RechazarReservaView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    UpdateView
):

    model = Reserva

    fields = []

    success_url = reverse_lazy('lista')

    def test_func(self):

        return self.request.user.groups.filter(
            name='Administradores'
        ).exists()

    def post(self, request, *args, **kwargs):

        reserva = self.get_object()

        reserva.estado = 'rechazada'

        reserva.save()

        return redirect('lista')



def exportar_csv(request):

    response = HttpResponse(
        content_type='text/csv'
    )

    response[
        'Content-Disposition'
    ] = 'attachment; filename="reservas.csv"'

    writer = csv.writer(response)

    writer.writerow([
        'Usuario',
        'Laboratorio',
        'Fecha',
        'Hora Inicio',
        'Hora Fin',
        'Estado',
        'Motivo'
    ])

    reservas = Reserva.objects.all()

    for r in reservas:

        writer.writerow([
            r.usuario.username,
            r.laboratorio,
            r.fecha,
            r.hora_inicio,
            r.hora_fin,
            r.estado,
            r.motivo
        ])

    return response