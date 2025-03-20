from django.contrib import admin
from .models import (
    Usuarios, Proveedores, Materiales, ProductosTerminados, OrdenesProduccion,
    AsignacionMateriales, Ubicaciones, UbicacionStock, Entradas, Salidas,
    Inventario, Mermas, Notificaciones, Transferencias, AjustesInventario,
    HistorialMovimientos, Facturas, DetallesFactura, Inspecciones
)


admin.site.register(Usuarios)
admin.site.register(Proveedores)
admin.site.register(Materiales)
admin.site.register(ProductosTerminados)
admin.site.register(OrdenesProduccion)
admin.site.register(AsignacionMateriales)
admin.site.register(Ubicaciones)
admin.site.register(UbicacionStock)
admin.site.register(Entradas)
admin.site.register(Salidas)
admin.site.register(Inventario)
admin.site.register(Mermas)
admin.site.register(Notificaciones)
admin.site.register(Transferencias)
admin.site.register(AjustesInventario)
admin.site.register(HistorialMovimientos)
admin.site.register(Facturas)
admin.site.register(DetallesFactura)
admin.site.register(Inspecciones)