from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Producto(models.Model):
    nombre= models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField(blank=True, null=True)
    stock = models.IntegerField()

    def __str__(self):
        return self.nombre


class Carrito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    productos = models.ManyToManyField(Producto, through='DetalleCarrito')

    def __str__(self):
        return f'Carrito de {self.usuario}'
    

class DetalleCarrito(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

    def __str__(self):
        return f'{self.cantidad} x {self.producto.nombre} en el carrito'