from django.shortcuts import render, redirect
from .models import Flan
from .forms import ContactFormForm, UsuarioForm
#from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.models import User
from .forms import RegistroForm


""" def index(request):
    return render(request, 'index.html') """

def about(request):
    return render(request, 'about.html')

def pagina(request):
    return render(request, 'pagina.html')

def exito(request):
    return render(request, 'form_exito.html')

#COMPRUEBA EL TIPO DE PETICION HTTP DEL MODELO CONTACTOFORM Y COMPRUEBA SI ES VALIDO,SI LO ES, LO ENVIA A LA BD Y REDIRIGE A EL HTML ""
def contacto(request):
    if request.method == 'POST':
        form = ContactFormForm(request.POST) # crea una instancia form y la pobla con la data del request. 
        if form.is_valid():
            form.save()
            return redirect('/exito') #redirige a la vista exito que lleva a form_exito.html
    else:
        form = ContactFormForm()
    return render(request, 'contacto.html', {'form': form}) #si no hay un formulario valido, renderiza el contacto.html


# Obtener los flanes publicos
def index(request):
    flanes_publicos = Flan.objects.filter(is_private=False)
    context = {
        'flanes': flanes_publicos
    }
    return render(request, 'index.html', context)

# Obtener los flanes privados
@login_required
def welcome(request):
    #flanes_privados = Flan.objects.filter(is_private=True)
    #mostrar_todos hace que muestre todos los productos (flanes) que estan en la bd
    mostrar_todos = Flan.objects.all()
    context = {
        'flanes': mostrar_todos
    }
    return render(request, 'welcome.html', context)


# AGREGAR USUARIO
def registro_usuario(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            #usuario = form.save(commit=False) #queda en stand by y no se guarda aun en la bd
            #usuario.set_clave(form.cleaned_data['clave'])
            #usuario.save()
            user = form.save()
            login(request, user)
            return redirect('/exito') #redirige a la vista exito que lleva a form_exito.html
    else:
        form = RegistroForm()
    return render(request, 'registration/registro_usuario.html', {'form': form})
