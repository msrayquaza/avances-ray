from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UsuariosViewSet, ProveedoresViewSet, MaterialesViewSet,
    ProductosTerminadosViewSet, OrdenesProduccionViewSet,
    AsignacionMaterialesViewSet, UbicacionesViewSet, UbicacionStockViewSet,
    EntradasViewSet, SalidasViewSet, InventarioViewSet, MermasViewSet,
    NotificacionesViewSet, TransferenciasViewSet, AjustesInventarioViewSet,
    HistorialMovimientosViewSet, FacturasViewSet, DetallesFacturaViewSet,
    InspeccionesViewSet, LogoutView
)
from .views import RegisterView, LoginView, UsuarioInfoView

router = DefaultRouter()
router.register(r'usuarios', UsuariosViewSet)
router.register(r'proveedores', ProveedoresViewSet)
router.register(r'materiales', MaterialesViewSet)
router.register(r'productos-terminados', ProductosTerminadosViewSet)
router.register(r'ordenes-produccion', OrdenesProduccionViewSet)
router.register(r'asignacion-materiales', AsignacionMaterialesViewSet)
router.register(r'ubicaciones', UbicacionesViewSet)
router.register(r'ubicacion-stock', UbicacionStockViewSet)
router.register(r'entradas', EntradasViewSet)
router.register(r'salidas', SalidasViewSet)
router.register(r'inventario', InventarioViewSet)
router.register(r'mermas', MermasViewSet)
router.register(r'notificaciones', NotificacionesViewSet)
router.register(r'transferencias', TransferenciasViewSet)
router.register(r'ajustes-inventario', AjustesInventarioViewSet)
router.register(r'historial-movimientos', HistorialMovimientosViewSet)
router.register(r'facturas', FacturasViewSet)
router.register(r'detalles-factura', DetallesFacturaViewSet)
router.register(r'inspecciones', InspeccionesViewSet)

urlpatterns = [ 
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path("usuario_info/", UsuarioInfoView.as_view(), name="usuario_info"),
]