from django.db import models
from django.utils.text import slugify
import uuid #importacion de estándar de generación de identificadores únicos
from django.contrib.auth.hashers import make_password,check_password #encripta y chequea las passwords
from django.contrib.auth.models import User

#CLASE PARA LA CREACION DE PRODUCTOS (flan)
class Flan(models.Model):
    flan_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=64)
    description = models.TextField()
    image_url = models.URLField(default='https://eurelec.pt/img/noimage.jpg')
    slug = models.SlugField(unique=True, blank=True)
    is_private = models.BooleanField(default=False)
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Nuevo campo


    class Meta:
        verbose_name = "Flan"
        verbose_name_plural = "Productos (Flanes)"


    def save(self, *args, **kwargs):
        self.name = self.name.capitalize()
        self.description = self.description.capitalize()
        if not self.slug:
            self.slug = slugify(self.name)
            while Flan.objects.filter(slug=self.slug).exists():
                self.slug = f"{self.slug}-{str(uuid.uuid4())[:8]}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    

# CLASE PARA LOS FORMULARIOS

#Formulario de contacto
class ContactForm(models.Model):
    contact_form_uuid = models.UUIDField(default=uuid.uuid4, editable=False) #define un UUID en su versión 4(al azar) cada vez que se genere un nuevo registro del modelo ContactForm.
    customer_email = models.EmailField()
    customer_name = models.CharField(max_length=64)
    message = models.TextField()

    class Meta:
        verbose_name = "Formulario de Contacto"
        verbose_name_plural = "Formularios de Contacto"

    def __str__(self) -> str:
        return self.customer_name
    
#Registro de usuarios
class UsuarioForm (models.Model):
    nombre = models.CharField(max_length=200)
    fecha_nacimiento = models.DateField()
    email = models.EmailField(primary_key=True)
    clave = models.CharField(max_length=128)
    

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Registro de Usuarios"

    def __str__(self) -> str:
        return self.nombre
    
    #metodo para encriptar clave
    def set_clave (self, raw_password):
        self.clave = make_password(raw_password)

    #metodo para comparar clave ingresada por el usuario contra la registrada en la bd
    def check_clave (self, raw_password):
        return check_password (raw_password, self.clave)
    

#MODELO DE PRODUCTOS DE PRUEBA 
class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    #imagen = models.ImageField(upload_to='productos/')
    image_url = models.URLField(default='https://eurelec.pt/img/noimage.jpg')


    def __str__(self):
        return self.nombre
    
class Carrito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Carrito de {self.usuario.username}"

class ItemCarrito(models.Model):
    producto = models.ForeignKey(Flan, on_delete=models.CASCADE)  # Cambia Producto a Flan
    carrito = models.ForeignKey(Carrito, related_name='items', on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    def subtotal(self):
        return self.cantidad * self.producto.precio

    def __str__(self):
        return f"{self.producto.name} x {self.cantidad}"