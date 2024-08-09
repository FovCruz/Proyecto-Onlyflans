from django.shortcuts import render, redirect, get_object_or_404
from .models import Flan, Producto, Carrito, ItemCarrito
from .forms import ContactFormForm, UsuarioForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.models import User
from .forms import RegistroForm

def about(request):
    return render(request, 'about.html')

def pagina(request):
    return render(request, 'pagina.html')

def exito(request):
    return render(request, 'form_exito.html')

def contacto(request):
    if request.method == 'POST':
        form = ContactFormForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/exito')
    else:
        form = ContactFormForm()
    return render(request, 'contacto.html', {'form': form})

def index(request):
    flanes_publicos = Flan.objects.filter(is_private=False)
    context = {
        'flanes': flanes_publicos
    }
    return render(request, 'index.html', context)

@login_required
def welcome(request):
    mostrar_todos = Flan.objects.all()
    context = {
        'flanes': mostrar_todos
    }
    return render(request, 'welcome.html', context)

def registro_usuario(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/exito')
    else:
        form = RegistroForm()
    return render(request, 'registration/registro_usuario.html', {'form': form})

@login_required
def agregar_al_carrito(request, flan_slug):
    flan = get_object_or_404(Flan, slug=flan_slug)
    cantidad = int(request.GET.get('cantidad', 1))  # Obtener la cantidad desde la solicitud GET
    carrito, created = Carrito.objects.get_or_create(usuario=request.user)
    
    item, created = ItemCarrito.objects.get_or_create(carrito=carrito, producto=flan)

    if created:
        item.cantidad = cantidad  # Si es un nuevo item, se asigna la cantidad seleccionada
    else:
        item.cantidad += cantidad  # Si ya existe, se suma la cantidad seleccionada

    item.save()
    carrito.total += flan.precio * cantidad
    carrito.save()

    return redirect('ver_carrito')


@login_required
def ver_carrito(request):
    carrito, created = Carrito.objects.get_or_create(usuario=request.user)

    if carrito.items.count() == 0:
        carrito.total = 0.00
        carrito.save()
        empty_cart = True
    else:
        empty_cart = False

    return render(request, 'carrito.html', {'carrito': carrito, 'empty_cart': empty_cart})


@login_required
def actualizar_item(request, item_id, accion):
    item = get_object_or_404(ItemCarrito, id=item_id)
    if accion == 'aumentar':
        item.cantidad += 1
        item.carrito.total += item.producto.precio
    elif accion == 'disminuir':
        if item.cantidad > 1:
            item.cantidad -= 1
            item.carrito.total -= item.producto.precio
        elif item.cantidad == 1:
            # Si la cantidad es 1 y se presiona disminuir, se elimina el producto del carrito
            item.carrito.total -= item.producto.precio
            item.delete()
            return redirect('ver_carrito')

    item.save()
    item.carrito.save()
    return redirect('ver_carrito')


@login_required
def actualizar_cantidad_producto(request, flan_slug, accion):
    flan = get_object_or_404(Flan, slug=flan_slug)
    cantidad = int(request.GET.get('cantidad', 1))
    
    if accion == 'aumentar':
        cantidad += 1
    elif accion == 'disminuir' and cantidad > 0:
        cantidad -= 1

    total = flan.precio * cantidad

    context = {
        'flan': flan,
        'cantidad': cantidad,
        'total': total,
    }
    
    return render(request, 'producto_detalle.html', context)

def ver_producto(request, flan_slug):
    flan = get_object_or_404(Flan, slug=flan_slug)
    cantidad = 1
    total = flan.precio * cantidad
    return render(request, 'producto_detalle.html', {'flan': flan, 'cantidad': cantidad, 'total': total})
