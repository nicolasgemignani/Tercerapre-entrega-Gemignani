from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Carrito, DetalleCarrito
from .forms import ProductoForm, CarritoForm, DetalleCarritoForm, BusquedaProductoForm, BusquedaCarritoForm


# Create your views here.
def pag_pricipal(req):
    return render(req, 'padre.html', {})


def detalle_producto(req, producto_id):
    producto = Producto.objects.get(id=producto_id)
    return render(req, 'productos/detalle_producto.html', {'producto': producto})


def crear_producto(req):
    if req.method == 'POST':
        form = ProductoForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('buscar_producto')
    else:
        form = ProductoForm()
    return render(req, 'forms/crear_producto.html', { 'form': form})


def crear_carrito(req):
    if req.method == 'POST':
        form = CarritoForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('buscar_producto')
    else:
        form = CarritoForm()
    
    return render(req, 'forms/crear_carrito.html', { 'form': form})


def crear_detalle_carrito(req):
    if req.method == 'POST':
        form = DetalleCarritoForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('crear_detalle_carrito')
    else:
        form = DetalleCarritoForm()
    
    return render(req, 'forms/crear_detalle_carrito.html', { 'form': form})

def buscar_producto(req):
    productos = []
    form = BusquedaProductoForm()

    if req.method == 'GET':
        form = BusquedaProductoForm(req.GET)
        if form.is_valid():
            query = form.cleaned_data['query']      
            productos = Producto.objects.filter(nombre__icontains=query)   

    return render(req, 'forms/buscar_productos.html', {'form': form, 'productos': productos })

def mostrar_carrito(request, carrito_id):
    carrito = get_object_or_404(Carrito, id=carrito_id)
    detalles_carrito = DetalleCarrito.objects.filter(carrito=carrito)

    # Calcular el total del carrito y el total por producto
    total = 0
    detalles_con_totales = []
    
    for detalle in detalles_carrito:
        subtotal = detalle.producto.precio * detalle.cantidad
        total += subtotal
        detalles_con_totales.append((detalle, subtotal))

    return render(request, 'carrito/detalle_carrito.html', {
        'carrito': carrito,
        'detalles_con_totales': detalles_con_totales,  # Pasar detalles con subtotal
        'total': total,
    })


def buscar_carrito(req):
    carritos = []
    form = BusquedaCarritoForm()
    if req.method == 'GET':
        form = BusquedaCarritoForm(req.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            carritos = Carrito.objects.filter(usuario__username__icontains=query)
    return render(req, 'forms/buscar_carrito.html', {'form': form, 'carritos': carritos})
