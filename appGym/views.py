from django.shortcuts import render
from .models import profesor, clase, cliente
from .form import profesorForm, claseForm, clienteForm


def inicio(request):
    return render(request, 'appGym/padre.html')

def profesorFormulario(request):

    if request.method=='POST':
        form=profesorForm(request.POST)
        if form.is_valid():
            diccionario=form.cleaned_data
            nombre=diccionario['nombre']
            apellido=diccionario['apellido']
            profesion=diccionario['profesion']
            anio=diccionario['anio_experiencia']
            fecha=diccionario['fecha_nacimiento']
            email=diccionario['email']
            entrenador=profesor(nombre=nombre, apellido=apellido, profesion=profesion, anio_experiencia=anio, fecha_nacimiento=fecha, email=email)
            entrenador.save()

            return render(request, 'appGym/profesoresFormulario.html', {'mensaje':'Agregaste un profesor correctamente!'})

        else:
            formulario=profesorForm()
            return render(request, 'appGym/profesoresFormulario.html', {'form':formulario})

    else:
        formulario=profesorForm()

    return render(request, 'appGym/profesoresFormulario.html', {'form':formulario})


def claseFormulario(request):

    if request.method=='POST':
        form=claseForm(request.POST)
        if form.is_valid():
            diccionario=form.cleaned_data
            nombre=diccionario['nombre']
            intensidad=diccionario['intensidad']
            entrenamiento=clase(nombre=nombre, intensidad=intensidad)
            entrenamiento.save()

            return render(request, 'appGym/claseFormulario.html', {'mensaje':'Agregaste una clase correctamente!'})

        else:
            return render(request, 'appGym/claseFormulario.html', {'mensaje':'Ingresaste una clase incorrectamente'})

    else:
        formulario=claseForm()

    return render(request, 'appGym/claseFormulario.html', {'form':formulario})



def clienteFormulario(request):

    if request.method=='POST':
        form=clienteForm(request.POST)
        if form.is_valid():
            diccionario=form.cleaned_data
            nombre=diccionario['nombre']
            apellido=diccionario['apellido']
            genero=diccionario['genero']
            antiguedad=diccionario['antiguedad']
            fecha=diccionario['fecha_nacimiento']
            email=diccionario['email']
            client=cliente(nombre=nombre, apellido=apellido, genero=genero, antiguedad=antiguedad, fecha_nacimiento=fecha, email=email)
            client.save()

            return render(request, 'appGym/clienteFormulario.html', {'mensaje':'Agregaste un cliente correctamente!'})

        else:
            return render(request, 'appGym/clienteFormulario.html', {'mensaje':'Ingresaste un cliente incorrectamente'})

    else:
        formulario=clienteForm()

    return render(request, 'appGym/clienteFormulario.html', {'form':formulario})


def busquedaProfesor(request):
    return render(request, 'appGym/profesores.html')


def busquedaProfesorResultado(request):
    if request.GET['nombre']:
        unnombre=request.GET['nombre']
        profes=profesor.objects.filter(nombre=unnombre)
        return render(request, 'appGym/resultadoProfesores.html', {'profes':profes})

    else:
        return render(request, 'appGym/profesores.html', {'mensaje':'Ingresa un valor correcto'})


def busquedaClase(request):
    return render(request, 'appGym/clases.html')


def busquedaClaseResultado(request):
    if request.GET['nombre']:
        unnombre=request.GET['nombre']
        clases=clase.objects.filter(nombre=unnombre)
        return render(request, 'appGym/resultadoClases.html', {'clases':clases})

    else:
        return render(request, 'appGym/clases.html', {'mensaje':'Ingresa un valor correcto'})


def busquedaCliente(request):
    return render(request, 'appGym/clientes.html')


def busquedaClienteResultado(request):
    if request.GET['nombre']:
        unnombre=request.GET['nombre']
        clientes=cliente.objects.filter(nombre=unnombre)
        return render(request, 'appGym/resultadoClientes.html', {'clientes':clientes})

    else:
        return render(request, 'appGym/clientes.html', {'mensaje':'Ingresa un valor correcto'})