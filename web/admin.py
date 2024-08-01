from django.contrib import admin
from .models import Flanes

# Register your models here.

#REGISTRO GENERICO (vista desde el panel de admin )
#admin.site.register(Flanes)

#REGISTRO PERSONALIZADO (vista desde el panel "Flanes" )
@admin.register(Flanes)
class FlanesAdmin(admin.ModelAdmin):
    list_display = ('name','description','slug','is_private')
    search_fields = ('name','name')
    list_filter = ('is_private','name')
    