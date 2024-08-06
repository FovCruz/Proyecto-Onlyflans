from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('acerca/', views.about , name='about'),
    path('bienvenido/', views.welcome, name='welcome'),
    path('contacto/', views.contacto, name='contacto'),
    path('exito/', views.exito, name='exito'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('registro/', views.agregar_usuario, name='agregar_usuario'),

    
]
