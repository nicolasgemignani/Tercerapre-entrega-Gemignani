"""
URL configuration for entrega3 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import pag_pricipal, detalle_producto, crear_producto, crear_carrito, crear_detalle_carrito, buscar_producto, buscar_carrito, mostrar_carrito

urlpatterns = [
    path('', pag_pricipal),
    path('producto/<int:producto_id>', detalle_producto, name = 'detalle_producto'),
    path('producto/crear/', crear_producto, name = 'crear_producto'),
    path('carrito/crear/', crear_carrito, name = 'crear_carrito'),
    path('detalle_carrito/crear/', crear_detalle_carrito, name = 'crear_detalle_carrito'),
    path('buscar-producto/', buscar_producto, name = 'buscar_producto'),
    path('carritos/<int:carrito_id>/', mostrar_carrito, name='mostrar_carrito'),
    path('buscar-carrito/', buscar_carrito, name='buscar_carrito')
]
