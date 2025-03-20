import os
import django
from django.utils import timezone

# Configura Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stockquery.settings')
django.setup()

from almacen.models import (
    Usuarios, Proveedores, Materiales, ProductosTerminados, OrdenesProduccion,
    AsignacionMateriales, Ubicaciones, UbicacionStock, Entradas, Salidas,
    Inventario, Mermas, Notificaciones, Transferencias, AjustesInventario,
    HistorialMovimientos, Facturas, DetallesFactura, Inspecciones
)

def populate():
    # Crear usuarios
    admin = Usuarios.objects.create(
        nombre="Admin",
        correo="admin@example.com",
        contraseña="hashed_password_123",
        rol="Administrador",
        activo=True
    )

    operador = Usuarios.objects.create(
        nombre="Operador",
        correo="operador@example.com",
        contraseña_hash="hashed_password_456",
        rol="Operador",
        activo=True
    )

    # Crear proveedores
    proveedor_a = Proveedores.objects.create(
        nombre="Proveedor A",
        contacto="Juan Pérez",
        telefono="123456789",
        correo="proveedorA@example.com",
        direccion="Calle Falsa 123"
    )

    proveedor_b = Proveedores.objects.create(
        nombre="Proveedor B",
        contacto="María Gómez",
        telefono="987654321",
        correo="proveedorB@example.com",
        direccion="Avenida Siempre Viva 456"
    )

    # Crear materiales
    acero = Materiales.objects.create(
        nombre="Acero",
        descripcion="Material resistente",
        unidad_medida="kg",
        punto_reorden=100
    )

    plastico = Materiales.objects.create(
        nombre="Plástico",
        descripcion="Material ligero",
        unidad_medida="kg",
        punto_reorden=200
    )

    # Crear productos terminados
    producto_a = ProductosTerminados.objects.create(
        nombre="Producto A",
        descripcion="Producto terminado de alta calidad",
        stock_actual=50,
        punto_reorden=20
    )

    producto_b = ProductosTerminados.objects.create(
        nombre="Producto B",
        descripcion="Producto terminado estándar",
        stock_actual=100,
        punto_reorden=30
    )

    # Crear órdenes de producción
    orden_a = OrdenesProduccion.objects.create(
        codigo_orden="ORD-001",
        descripcion="Orden de producción para el Producto A",
        estado="Pendiente"
    )

    orden_b = OrdenesProduccion.objects.create(
        codigo_orden="ORD-002",
        descripcion="Orden de producción para el Producto B",
        estado="En Progreso"
    )

    # Crear asignación de materiales
    AsignacionMateriales.objects.create(
        id_orden_produccion=orden_a,
        id_material=acero,
        cantidad=10
    )

    AsignacionMateriales.objects.create(
        id_orden_produccion=orden_b,
        id_material=plastico,
        cantidad=20
    )

    # Crear ubicaciones
    ubicacion_a = Ubicaciones.objects.create(
        almacen="Almacén Central",
        pasillo="A",
        rack="1",
        anaquel="1"
    )

    ubicacion_b = Ubicaciones.objects.create(
        almacen="Almacén Secundario",
        pasillo="B",
        rack="2",
        anaquel="2"
    )

    # Crear ubicación de stock
    UbicacionStock.objects.create(
        id_material=acero,
        id_ubicacion=ubicacion_a,
        cantidad=500
    )

    UbicacionStock.objects.create(
        id_producto=producto_a,
        id_ubicacion=ubicacion_b,
        cantidad=100
    )

    # Crear entradas
    Entradas.objects.create(
        id_proveedor=proveedor_a,
        id_material=acero,
        cantidad=100,
        lote="LOTE-001",
        factura="FAC-001",
        id_ubicacion=ubicacion_a,
        inspeccionado=True,
        numero_serie="NS-001",
        id_usuario=admin
    )

    Entradas.objects.create(
        id_proveedor=proveedor_b,
        id_material=plastico,
        cantidad=200,
        lote="LOTE-002",
        factura="FAC-002",
        id_ubicacion=ubicacion_b,
        inspeccionado=False,
        numero_serie="NS-002",
        id_usuario=operador
    )

    # Crear salidas
    Salidas.objects.create(
        id_material=acero,
        cantidad=50,
        motivo="Producción",
        id_orden_produccion=orden_a,
        id_usuario=admin
    )

    Salidas.objects.create(
        id_producto=producto_a,
        cantidad=10,
        motivo="Ajuste",
        id_usuario=operador
    )

    # Crear inventario
    Inventario.objects.create(
        id_material=acero,
        id_ubicacion=ubicacion_a,
        cantidad=450
    )

    Inventario.objects.create(
        id_producto=producto_a,
        id_ubicacion=ubicacion_b,
        cantidad=90
    )

    # Crear mermas
    Mermas.objects.create(
        id_material=acero,
        cantidad=5,
        motivo="Dañado",
        id_usuario=admin
    )

    Mermas.objects.create(
        id_producto=producto_a,
        cantidad=2,
        motivo="Pérdida",
        id_usuario=operador
    )

    # Crear notificaciones
    Notificaciones.objects.create(
        mensaje="Stock de acero bajo",
        id_usuario=admin
    )

    Notificaciones.objects.create(
        mensaje="Nueva orden de producción creada",
        id_usuario=operador
    )

    # Crear transferencias
    Transferencias.objects.create(
        id_material=acero,
        cantidad=50,
        id_ubicacion_origen=ubicacion_a,
        id_ubicacion_destino=ubicacion_b,
        id_usuario=admin
    )

    Transferencias.objects.create(
        id_producto=producto_a,
        cantidad=10,
        id_ubicacion_origen=ubicacion_b,
        id_ubicacion_destino=ubicacion_a,
        id_usuario=operador
    )

    # Crear ajustes de inventario
    AjustesInventario.objects.create(
        id_material=acero,
        cantidad=10,
        motivo="Ajuste de inventario",
        id_usuario=admin
    )

    AjustesInventario.objects.create(
        id_producto=producto_a,
        cantidad=5,
        motivo="Ajuste de inventario",
        id_usuario=operador
    )

    # Crear historial de movimientos
    HistorialMovimientos.objects.create(
        id_material=acero,
        tipo_movimiento="Entrada",
        cantidad=100,
        id_usuario=admin
    )

    HistorialMovimientos.objects.create(
        id_producto=producto_a,
        tipo_movimiento="Salida",
        cantidad=10,
        id_usuario=operador
    )

    # Crear facturas
    factura_a = Facturas.objects.create(
        numero_factura="FAC-001",
        id_proveedor=proveedor_a
    )

    factura_b = Facturas.objects.create(
        numero_factura="FAC-002",
        id_proveedor=proveedor_b
    )

    # Crear detalles de factura
    DetallesFactura.objects.create(
        id_factura=factura_a,
        id_material=acero,
        cantidad=100
    )

    DetallesFactura.objects.create(
        id_factura=factura_b,
        id_material=plastico,
        cantidad=200
    )

    # Crear inspecciones
    Inspecciones.objects.create(
        id_material=acero,
        id_proveedor=proveedor_a,
        resultado="Aprobado",
        observaciones="Material en buen estado"
    )

    Inspecciones.objects.create(
        id_material=plastico,
        id_proveedor=proveedor_b,
        resultado="Rechazado",
        observaciones="Material defectuoso"
    )

    print("Base de datos poblada exitosamente.")

if __name__ == '__main__':
    populate()