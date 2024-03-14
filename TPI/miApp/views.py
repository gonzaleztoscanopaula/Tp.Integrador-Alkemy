from django.shortcuts import render, redirect
from .models import Proveedor, Producto
from .forms import ProveedorForm, ProductoForm
from django.contrib import messages


def agregar_proveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            # Guardar el proveedor en la base de datos
            proveedor = form.save()
            # Mostrar mensaje de éxito
            messages.success(request, 'Proveedor agregado con éxito.')
            # Redirigir a una página que muestre el mensaje de éxito
            return redirect('proveedor_agregado_exitosamente', proveedor_id=proveedor.id)  
    else:
        form = ProveedorForm()
    return render(request, 'agregar_proveedor.html', {'form': form})

def proveedor_agregado_exitosamente(request, proveedor_id):
    proveedor = Proveedor.objects.get(pk=proveedor_id)
    return render(request, 'proveedor_agregado_exitosamente.html', {'proveedor': proveedor})

def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            # Guardar el producto en la base de datos
            producto = form.save()
            # Mostrar mensaje de éxito
            messages.success(request, 'Producto agregado con éxito.')
            # Redirigir a una página que muestre el mensaje de éxito y detalle del producto
            return redirect('producto_agregado_exitosamente', producto_id=producto.id)
    else:
        form = ProductoForm()
    return render(request, 'agregar_producto.html', {'form': form})

def producto_agregado_exitosamente(request, producto_id):
    producto = Producto.objects.get(pk=producto_id)
    return render(request, 'producto_agregado_exitosamente.html', {'producto': producto})

def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'listar_productos.html', {'productos': productos})

def listar_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'listar_proveedores.html', {'proveedores': proveedores})

# Create your views here.

