from django import forms
from .models import Producto, Carrito, DetalleCarrito

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'descripcion', 'stock']


class CarritoForm(forms.ModelForm):
    class Meta:
        model = Carrito
        fields = ['usuario']


class DetalleCarritoForm(forms.ModelForm):
    class Meta:
        model = DetalleCarrito
        fields = ['carrito', 'producto', 'cantidad']


class BusquedaProductoForm(forms.Form):
    query = forms.CharField(label='Buscar Producto', max_length=200, required=False)


class BusquedaCarritoForm(forms.Form):
    query = forms.CharField(label='Buscar Carrito', max_length=100, required=False)