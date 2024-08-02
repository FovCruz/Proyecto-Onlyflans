from django.shortcuts import render, redirect
from .models import Flanes
from .forms import ContactFormForm
from django.http import HttpResponse

""" def index(request):
    return render(request, 'index.html') """

def about(request):
    return render(request, 'about.html')

def pagina(request):
    return render(request, 'pagina.html')

def exito(request):
    return render(request, 'form_exito.html')

# DEFINE VISTA QUE COMPRUEBA EL TIPO DE PETICION HTTP DEL MODELO CONTACTOFORM Y COMPRUEBA SI ES VALIDO,SI LO ES, LO ENVIA A LA BD Y REDIRIGE A EL HTML ""
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
    flanes_publicos = Flanes.objects.filter(is_private=False)
    context = {
        'flanes': flanes_publicos
    }
    return render(request, 'index.html', context)

# Obtener los flanes privados
def welcome(request):
    flanes_privados = Flanes.objects.filter(is_private=True)
    context = {
        'flanes': flanes_privados
    }
    return render(request, 'welcome.html', context)