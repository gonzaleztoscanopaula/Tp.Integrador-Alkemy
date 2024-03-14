"""
URL configuration for TPI project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from miApp import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('agregar_proveedor/', views.agregar_proveedor, name='agregar_proveedor'),
    path('agregar_producto/', views.agregar_producto, name='agregar_producto'),
    path('listar_productos/', views.listar_productos, name='listar_productos'),
    path('listar_proveedores/', views.listar_proveedores, name='listar_proveedores'),
    path('proveedor_agregado_exitosamente/<int:proveedor_id>/', views.proveedor_agregado_exitosamente, name='proveedor_agregado_exitosamente'),
    path('producto_agregado_exitosamente/<int:producto_id>/', views.producto_agregado_exitosamente, name='producto_agregado_exitosamente'),
]
