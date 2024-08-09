from django.contrib import admin
from .models import Flan, ContactForm,UsuarioForm

# Register your models here.

#REGISTRO GENERICO (vista desde el panel de admin )
#admin.site.register(Flan)

#REGISTRO PERSONALIZADO (vista desde el panel "Productos (Flanes)" )
@admin.register(Flan)
class FlanAdmin(admin.ModelAdmin):
    list_display = ('name','description','slug','precio','is_private')
    search_fields = ('name','name')
    list_filter = ('is_private','name')

#REGISTRO PERSONALIZADO (vista desde el panel "formularios de contacto" )
@admin.register(ContactForm)
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ('customer_name','customer_email','message')
    search_fields = ('customer_email','customer_name')
    list_filter = ('customer_name','customer_email')
      

#REGISTRO PERSONALIZADO (vista desde el panel "Registro de usuarios" )
@admin.register(UsuarioForm)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('email','nombre','fecha_nacimiento')
    search_fields = ('email','nombre')
    list_filter = ('email','nombre')
      