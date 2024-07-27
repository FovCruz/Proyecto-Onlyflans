from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def welcome(request):
    return render(request, 'welcome.html')

def pagina(request):
    return render(request, 'pagina.html')