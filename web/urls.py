from django.urls import path, include
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('acerca/', views.about, name='about'),
    path('bienvenido/', views.welcome, name='welcome'),
    path('contacto/', views.contacto, name='contacto'),
    path('exito/', views.exito, name='exito'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('registro/', views.registro_usuario, name='registro_usuario'),
]
