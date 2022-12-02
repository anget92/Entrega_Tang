from django.urls import path
from appGym.views import *

urlpatterns = [
    path('', inicio, name='inicio'),
    path('formularioProfesores/', profesorFormulario, name='profesorFormulario'),
    path('formularioClase/', claseFormulario, name='claseFormulario'),
    path('formularioCliente/', clienteFormulario, name='clienteFormulario'),
    path('buscarProfesor/', busquedaProfesor, name='buscarProfesor'),
    path('buscarProfesorResultado/', busquedaProfesorResultado, name='buscarProfesorResultado'),
    path('buscarClase/', busquedaClase, name='buscarClase'),
    path('buscarClaseResultado/', busquedaClaseResultado, name='buscarClaseResultado'),
    path('buscarCliente/', busquedaCliente, name='buscarCliente'),
    path('buscarClienteResultado/', busquedaClienteResultado, name='buscarClienteResultado'),
    

]