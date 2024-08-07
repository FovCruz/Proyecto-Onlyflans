from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import ContactForm, UsuarioForm

# CLASE PARA CONFIGURAR FORMS DE CONTACTO 
class ContactFormForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = "__all__"  # traer todos los campos
        # fields = ['customer_email', 'customer_name', 'message'] # traer campos específicos
        widgets = {
            'customer_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'customer_name': forms.TextInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
        labels = {
            'customer_email': 'Correo',
            'customer_name': 'Nombre',
            'message': 'Mensaje',
        }
        label_attrs = {
            'customer_email': {'class': 'custom-label'},
            'customer_name': {'class': 'custom-label'},
            'message': {'class': 'custom-label'},
        }

# CLASE PARA CONFIGURAR FORMS DE REGISTRO DE USUARIOS 
class UsuarioForm(forms.ModelForm):
    class Meta:
        model = UsuarioForm
        fields = "__all__"  # traer todos los campos
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off'}),
            'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'autocomplete': 'off'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'autocomplete': 'off'}),
            'clave': forms.PasswordInput(attrs={'class': 'form-control', 'autocomplete': 'off'}),
        }
        labels = {
            'email': 'Correo',
            'nombre': 'Nombre',
            'fecha_nacimiento': 'Fecha de Nacimiento',
            'clave': 'Contraseña'
        }
        label_attrs = {
            'email': {'class': 'custom-label'},
            'nombre': {'class': 'custom-label'},
            'fecha_nacimiento': {'class': 'custom-label'},
        }

class RegistroForm(UserCreationForm):

    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    def __init__(self, *args, **kwargs):
        super(RegistroForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'autocomplete': 'off'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'autocomplete': 'off'})
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'autocomplete': 'off'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'autocomplete': 'off'})


