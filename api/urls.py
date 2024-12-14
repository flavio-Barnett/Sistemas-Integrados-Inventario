from rest_framework.routers import DefaultRouter
from .views import CategoriaViewSet, ProveedorViewSet, ProductoViewSet, TransaccionInventarioViewSet
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

# Configuración de la vista para la documentación
schema_view = get_schema_view(
    openapi.Info(
        title="API de Inventario",
        default_version='v1',
        description="Documentación de la API de Inventario",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="soporte@tuapp.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(AllowAny,),
)

# Configuración de las rutas de la API
router = DefaultRouter()
router.register('categorias', CategoriaViewSet)
router.register('proveedores', ProveedorViewSet)
router.register('productos', ProductoViewSet)
router.register('transacciones', TransaccionInventarioViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Endpoints principales
    # Endpoints para la documentación interactiva
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]