from django.shortcuts import render
from .models import Flanes
from django.http import HttpResponse

""" def index(request):
    return render(request, 'index.html') """

def about(request):
    return render(request, 'about.html')

def welcome(request):
    return render(request, 'welcome.html')

def pagina(request):
    return render(request, 'pagina.html')

def index(request):
    # Recuperar todos los flanes
    flanes_publicos = Flanes.objects.filter(is_private=False)
    # Pasar los flanes al contexto del template
    context = {
        'flanes': flanes_publicos
    }
    return render(request, 'index.html', context)