from rest_framework import viewsets
from .models import Categoria, Proveedor, Producto, TransaccionInventario
from .serializers import CategoriaSerializer, ProveedorSerializer, ProductoSerializer, TransaccionInventarioSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


class TransaccionInventarioViewSet(viewsets.ModelViewSet):
    queryset = TransaccionInventario.objects.all()
    serializer_class = TransaccionInventarioSerializer