from django import forms

class profesorForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    profesion=forms.CharField(max_length=50)
    anio_experiencia=forms.IntegerField()
    fecha_nacimiento=forms.DateField()
    email=forms.EmailField()

class claseForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    intensidad=forms.CharField(max_length=50)
    
class clienteForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    genero=forms.CharField(max_length=50)
    antiguedad=forms.IntegerField()
    fecha_nacimiento=forms.DateField()
    email=forms.EmailField()