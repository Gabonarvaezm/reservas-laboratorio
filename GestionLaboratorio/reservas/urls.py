from django.urls import path

from .views import (
    registro_docente,
    registro_administrador,
    login_view,
    logout_view,
    ReservaListView,
    ReservaCreateView,
    ReservaUpdateView,
    ReservaDeleteView,
    AprobarReservaView,
    RechazarReservaView,
    exportar_csv
)

urlpatterns = [

    path(
        '',
        ReservaListView.as_view(),
        name='lista'
    ),

    path(
        'registro-docente/',
        registro_docente.as_view(),
        name='registro_docente'
    ),

    path(
        'registro-administrador/',
        registro_administrador.as_view(),
        name='registro_administrador'
    ),

    path(
        'login/',
        login_view.as_view(),
        name='login'
    ),

    path(
        'logout/',
        logout_view.as_view(),
        name='logout'
    ),

    path(
        'crear/',
        ReservaCreateView.as_view(),
        name='crear'
    ),

    path(
        'editar/<int:pk>/',
        ReservaUpdateView.as_view(),
        name='editar'
    ),

    path(
        'eliminar/<int:pk>/',
        ReservaDeleteView.as_view(),
        name='eliminar'
    ),

    path(
        'aprobar/<int:pk>/',
        AprobarReservaView.as_view(),
        name='aprobar'
    ),

    path(
        'rechazar/<int:pk>/',
        RechazarReservaView.as_view(),
        name='rechazar'
    ),

    path(
        'csv/',
        exportar_csv,
        name='csv'
    ),
]