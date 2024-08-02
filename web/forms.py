from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import ContactForm #se importa la clase ContactForm desde models.py (alojado en app web)


#CLASE PARA CREAR FORMULARIOS
class ContactFormForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['customer_email', 'customer_name', 'message']
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






class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    #clase interna de django proporciona datos o configuracion adicional#
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']