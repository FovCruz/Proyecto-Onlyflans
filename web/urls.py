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
    path('agregar-al-carrito/<slug:flan_slug>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('ver-carrito/', views.ver_carrito, name='ver_carrito'),
    path('actualizar-item/<int:item_id>/<str:accion>/', views.actualizar_item, name='actualizar_item'),
    path('producto/<slug:flan_slug>/actualizar/<str:accion>/', views.actualizar_cantidad_producto, name='actualizar_cantidad_producto'),
    path('producto/<slug:flan_slug>/', views.ver_producto, name='ver_producto'),
    ]

