from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

class Usuarios(models.Model):
    id_usuario = models.BigAutoField(primary_key=True)  
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=255)  
    rol = models.CharField(max_length=50, choices=[
        ('Administrador', 'Administrador'),
        ('Operador', 'Operador'),
        ('Supervisor', 'Supervisor'),
    ])
    activo = models.BooleanField(default=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    imagen_perfil = models.ImageField(upload_to='perfiles/', blank=True, null=True)

    def __str__(self):
        return self.nombre

class Proveedores(models.Model):
    id_proveedor = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    correo = models.EmailField(blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Materiales(models.Model):
    id_material = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    unidad_medida = models.CharField(max_length=50, blank=True, null=True)
    punto_reorden = models.IntegerField(validators=[MinValueValidator(0)])

    def __str__(self):
        return self.nombre

class ProductosTerminados(models.Model):
    id_producto = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    stock_actual = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    punto_reorden = models.IntegerField(default=0, validators=[MinValueValidator(0)])

    def __str__(self):
        return self.nombre

class OrdenesProduccion(models.Model):
    ESTADO_CHOICES = [
        ('Pendiente', 'Pendiente'),
        ('En Progreso', 'En Progreso'),
        ('Completada', 'Completada'),
    ]

    id_orden_produccion = models.BigAutoField(primary_key=True)
    codigo_orden = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    fecha_inicio = models.DateTimeField(auto_now_add=True)
    fecha_fin = models.DateTimeField(blank=True, null=True)
    estado = models.CharField(max_length=50, choices=ESTADO_CHOICES)

    def __str__(self):
        return self.codigo_orden

class AsignacionMateriales(models.Model):
    id_asignacion = models.BigAutoField(primary_key=True)
    id_orden_produccion = models.ForeignKey(OrdenesProduccion, on_delete=models.CASCADE)
    id_material = models.ForeignKey(Materiales, on_delete=models.CASCADE)
    cantidad = models.IntegerField(validators=[MinValueValidator(1)])

    def __str__(self):
        return f"Asignación {self.id_asignacion}"

class Ubicaciones(models.Model):
    id_ubicacion = models.BigAutoField(primary_key=True)
    almacen = models.CharField(max_length=100)
    pasillo = models.CharField(max_length=50, blank=True, null=True)
    rack = models.CharField(max_length=50, blank=True, null=True)
    anaquel = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.almacen} - {self.pasillo} - {self.rack} - {self.anaquel}"

class UbicacionStock(models.Model):
    id_ubicacion_stock = models.BigAutoField(primary_key=True)
    id_material = models.ForeignKey(Materiales, on_delete=models.CASCADE, blank=True, null=True)
    id_producto = models.ForeignKey(ProductosTerminados, on_delete=models.CASCADE, blank=True, null=True)
    id_ubicacion = models.ForeignKey(Ubicaciones, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=0, validators=[MinValueValidator(0)])

    def __str__(self):
        return f"Ubicación Stock {self.id_ubicacion_stock}"

class Entradas(models.Model):
    id_entrada = models.BigAutoField(primary_key=True)
    id_proveedor = models.ForeignKey(Proveedores, on_delete=models.CASCADE, blank=True, null=True)
    id_material = models.ForeignKey(Materiales, on_delete=models.CASCADE)
    cantidad = models.IntegerField(validators=[MinValueValidator(1)])
    fecha_entrada = models.DateTimeField(auto_now_add=True)
    lote = models.CharField(max_length=100, blank=True, null=True)
    factura = models.CharField(max_length=100, blank=True, null=True)
    id_ubicacion = models.ForeignKey(Ubicaciones, on_delete=models.CASCADE)
    inspeccionado = models.BooleanField(default=False)
    numero_serie = models.CharField(max_length=100, blank=True, null=True)
    id_usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)

    def __str__(self):
        return f"Entrada {self.id_entrada}"

class Salidas(models.Model):
    MOTIVO_CHOICES = [
        ('Producción', 'Producción'),
        ('Dañado', 'Dañado'),
        ('Pérdida', 'Pérdida'),
        ('Ajuste', 'Ajuste'),
    ]

    id_salida = models.BigAutoField(primary_key=True)
    id_material = models.ForeignKey(Materiales, on_delete=models.CASCADE, blank=True, null=True)
    id_producto = models.ForeignKey(ProductosTerminados, on_delete=models.CASCADE, blank=True, null=True)
    cantidad = models.IntegerField(validators=[MinValueValidator(1)])
    fecha_salida = models.DateTimeField(auto_now_add=True)
    motivo = models.CharField(max_length=100, choices=MOTIVO_CHOICES)
    id_orden_produccion = models.ForeignKey(OrdenesProduccion, on_delete=models.CASCADE, blank=True, null=True)
    id_usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)

    def __str__(self):
        return f"Salida {self.id_salida}"

class Inventario(models.Model):
    id_inventario = models.BigAutoField(primary_key=True)
    id_material = models.ForeignKey(Materiales, on_delete=models.CASCADE, blank=True, null=True)
    id_producto = models.ForeignKey(ProductosTerminados, on_delete=models.CASCADE, blank=True, null=True)
    id_ubicacion = models.ForeignKey(Ubicaciones, on_delete=models.CASCADE)
    cantidad = models.IntegerField(validators=[MinValueValidator(0)])
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Inventario {self.id_inventario}"

class Mermas(models.Model):
    id_merma = models.BigAutoField(primary_key=True)
    id_material = models.ForeignKey(Materiales, on_delete=models.CASCADE, blank=True, null=True)
    id_producto = models.ForeignKey(ProductosTerminados, on_delete=models.CASCADE, blank=True, null=True)
    cantidad = models.IntegerField(validators=[MinValueValidator(1)])
    fecha_merma = models.DateTimeField(auto_now_add=True)
    motivo = models.CharField(max_length=100)
    id_usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)

    def __str__(self):
        return f"Merma {self.id_merma}"

class Notificaciones(models.Model):
    id_notificacion = models.BigAutoField(primary_key=True)
    mensaje = models.TextField()
    fecha_notificacion = models.DateTimeField(auto_now_add=True)
    id_usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    leida = models.BooleanField(default=False)

    def __str__(self):
        return f"Notificación {self.id_notificacion}"

class Transferencias(models.Model):
    id_transferencia = models.BigAutoField(primary_key=True)
    id_material = models.ForeignKey(Materiales, on_delete=models.CASCADE, blank=True, null=True)
    id_producto = models.ForeignKey(ProductosTerminados, on_delete=models.CASCADE, blank=True, null=True)
    cantidad = models.IntegerField(validators=[MinValueValidator(1)])
    fecha_transferencia = models.DateTimeField(auto_now_add=True)
    id_ubicacion_origen = models.ForeignKey(Ubicaciones, related_name='transferencias_origen', on_delete=models.CASCADE)
    id_ubicacion_destino = models.ForeignKey(Ubicaciones, related_name='transferencias_destino', on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)

    def __str__(self):
        return f"Transferencia {self.id_transferencia}"

class AjustesInventario(models.Model):
    id_ajuste = models.BigAutoField(primary_key=True)
    id_material = models.ForeignKey(Materiales, on_delete=models.CASCADE, blank=True, null=True)
    id_producto = models.ForeignKey(ProductosTerminados, on_delete=models.CASCADE, blank=True, null=True)
    cantidad = models.IntegerField(validators=[MinValueValidator(1)])
    fecha_ajuste = models.DateTimeField(auto_now_add=True)
    motivo = models.CharField(max_length=100)
    id_usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)

    def __str__(self):
        return f"Ajuste {self.id_ajuste}"

class HistorialMovimientos(models.Model):
    TIPO_MOVIMIENTO_CHOICES = [
        ('Entrada', 'Entrada'),
        ('Salida', 'Salida'),
        ('Transferencia', 'Transferencia'),
        ('Ajuste', 'Ajuste'),
    ]

    id_movimiento = models.BigAutoField(primary_key=True)
    id_material = models.ForeignKey(Materiales, on_delete=models.CASCADE, blank=True, null=True)
    id_producto = models.ForeignKey(ProductosTerminados, on_delete=models.CASCADE, blank=True, null=True)
    tipo_movimiento = models.CharField(max_length=50, choices=TIPO_MOVIMIENTO_CHOICES)
    cantidad = models.IntegerField(validators=[MinValueValidator(1)])
    fecha_movimiento = models.DateTimeField(auto_now_add=True)
    id_usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)

    def __str__(self):
        return f"Movimiento {self.id_movimiento}"

class Facturas(models.Model):
    id_factura = models.BigAutoField(primary_key=True)
    numero_factura = models.CharField(max_length=50, unique=True)
    id_proveedor = models.ForeignKey(Proveedores, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Factura {self.numero_factura}"

class DetallesFactura(models.Model):
    id_detalle = models.BigAutoField(primary_key=True)
    id_factura = models.ForeignKey(Facturas, on_delete=models.CASCADE)
    id_material = models.ForeignKey(Materiales, on_delete=models.CASCADE)
    cantidad = models.IntegerField(validators=[MinValueValidator(1)])

    def __str__(self):
        return f"Detalle {self.id_detalle}"

class Inspecciones(models.Model):
    RESULTADO_CHOICES = [
        ('Aprobado', 'Aprobado'),
        ('Rechazado', 'Rechazado'),
    ]

    id_inspeccion = models.BigAutoField(primary_key=True)
    id_material = models.ForeignKey(Materiales, on_delete=models.CASCADE)
    id_proveedor = models.ForeignKey(Proveedores, on_delete=models.CASCADE)
    resultado = models.CharField(max_length=100, choices=RESULTADO_CHOICES)
    observaciones = models.TextField(blank=True, null=True)
    fecha_inspeccion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Inspección {self.id_inspeccion}"