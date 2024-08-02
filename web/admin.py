from django.contrib import admin
from .models import Flanes, ContactForm

# Register your models here.

#REGISTRO GENERICO (vista desde el panel de admin )
#admin.site.register(Flanes)

#REGISTRO PERSONALIZADO (vista desde el panel "Flanes" )
@admin.register(Flanes)
class FlanesAdmin(admin.ModelAdmin):
    list_display = ('name','description','slug','is_private')
    search_fields = ('name','name')
    list_filter = ('is_private','name')

@admin.register(ContactForm)
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ('customer_name','customer_email','message')
    search_fields = ('customer_email','customer_name')
    list_filter = ('customer_name','customer_email')
      