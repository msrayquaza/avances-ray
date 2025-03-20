-- Creación de la base de datos
CREATE DATABASE IF NOT EXISTS StockManagement;
USE StockManagement;

-- Tabla de Usuarios  
CREATE TABLE Usuarios (
    id_usuario BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    correo VARCHAR(100) UNIQUE NOT NULL,
    contraseña VARCHAR(255) NOT NULL,
    rol VARCHAR(50) NOT NULL CHECK (rol IN ('Administrador', 'Operador', 'Supervisor')),
    activo BOOLEAN DEFAULT TRUE,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabla de Proveedores  
CREATE TABLE Proveedores (
    id_proveedor BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    contacto VARCHAR(100),
    telefono VARCHAR(20),
    correo VARCHAR(100),
    direccion TEXT
);

-- Tabla de Materiales  
CREATE TABLE Materiales (
    id_material BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    unidad_medida VARCHAR(50),
    punto_reorden INT
);

-- Tabla de Productos Terminados 
CREATE TABLE ProductosTerminados (
    id_producto BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    stock_actual INT DEFAULT 0,
    punto_reorden INT DEFAULT 0
);

-- Tabla de Órdenes de Producción  
CREATE TABLE OrdenesProduccion (
    id_orden_produccion BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    codigo_orden VARCHAR(50) UNIQUE NOT NULL,
    descripcion TEXT,
    fecha_inicio TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    fecha_fin TIMESTAMP,
    estado VARCHAR(50) CHECK (estado IN ('Pendiente', 'En Progreso', 'Completada'))
);

-- Tabla de Asignación de Materiales a Órdenes de Producción  
CREATE TABLE AsignacionMateriales (
    id_asignacion BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    id_orden_produccion BIGINT UNSIGNED NOT NULL,
    id_material BIGINT UNSIGNED NOT NULL,
    cantidad INT NOT NULL,
    FOREIGN KEY (id_orden_produccion) REFERENCES OrdenesProduccion(id_orden_produccion)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (id_material) REFERENCES Materiales(id_material)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

-- Tabla de Ubicaciones  
CREATE TABLE Ubicaciones (
    id_ubicacion BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    almacen VARCHAR(100) NOT NULL,
    pasillo VARCHAR(50),
    rack VARCHAR(50),
    anaquel VARCHAR(50)
);

-- Tabla de UbicacionStock 
CREATE TABLE UbicacionStock (
    id_ubicacion_stock BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    id_material BIGINT UNSIGNED,
    id_producto BIGINT UNSIGNED,
    id_ubicacion BIGINT UNSIGNED,
    cantidad INT NOT NULL DEFAULT 0,
    FOREIGN KEY (id_material) REFERENCES Materiales(id_material),
    FOREIGN KEY (id_producto) REFERENCES ProductosTerminados(id_producto),
    FOREIGN KEY (id_ubicacion) REFERENCES Ubicaciones(id_ubicacion)
);

-- Tabla de Entradas de Materiales  
CREATE TABLE Entradas (
    id_entrada BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    id_proveedor BIGINT UNSIGNED,
    id_material BIGINT UNSIGNED,
    cantidad INT NOT NULL,
    fecha_entrada TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    lote VARCHAR(100),
    factura VARCHAR(100),
    id_ubicacion BIGINT UNSIGNED,
    inspeccionado BOOLEAN DEFAULT FALSE,
    numero_serie VARCHAR(100),
    id_usuario BIGINT UNSIGNED,
    FOREIGN KEY (id_proveedor) REFERENCES Proveedores(id_proveedor),
    FOREIGN KEY (id_material) REFERENCES Materiales(id_material),
    FOREIGN KEY (id_ubicacion) REFERENCES Ubicaciones(id_ubicacion),
    FOREIGN KEY (id_usuario) REFERENCES Usuarios(id_usuario)
);

-- Tabla de Salidas de Materiales  
CREATE TABLE Salidas (
    id_salida BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    id_material BIGINT UNSIGNED,
    id_producto BIGINT UNSIGNED,
    cantidad INT NOT NULL,
    fecha_salida TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    motivo VARCHAR(100) CHECK (motivo IN ('Producción', 'Dañado', 'Pérdida', 'Ajuste')),
    id_orden_produccion BIGINT UNSIGNED,
    id_usuario BIGINT UNSIGNED,
    FOREIGN KEY (id_material) REFERENCES Materiales(id_material),
    FOREIGN KEY (id_producto) REFERENCES ProductosTerminados(id_producto),
    FOREIGN KEY (id_orden_produccion) REFERENCES OrdenesProduccion(id_orden_produccion),
    FOREIGN KEY (id_usuario) REFERENCES Usuarios(id_usuario)
);

-- Tabla de Inventario  
CREATE TABLE Inventario (
    id_inventario BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    id_material BIGINT UNSIGNED,
    id_producto BIGINT UNSIGNED,
    id_ubicacion BIGINT UNSIGNED,
    cantidad INT NOT NULL,
    fecha_actualizacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_material) REFERENCES Materiales(id_material),
    FOREIGN KEY (id_producto) REFERENCES ProductosTerminados(id_producto),
    FOREIGN KEY (id_ubicacion) REFERENCES Ubicaciones(id_ubicacion)
);

-- Tabla de Mermas  
CREATE TABLE Mermas (
    id_merma BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    id_material BIGINT UNSIGNED,
    id_producto BIGINT UNSIGNED,
    cantidad INT NOT NULL,
    fecha_merma TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    motivo VARCHAR(100),
    id_usuario BIGINT UNSIGNED,
    FOREIGN KEY (id_material) REFERENCES Materiales(id_material),
    FOREIGN KEY (id_producto) REFERENCES ProductosTerminados(id_producto),
    FOREIGN KEY (id_usuario) REFERENCES Usuarios(id_usuario)
);

-- Tabla de Notificaciones  
CREATE TABLE Notificaciones (
    id_notificacion BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    mensaje TEXT NOT NULL,
    fecha_notificacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    id_usuario BIGINT UNSIGNED,
    leida BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (id_usuario) REFERENCES Usuarios(id_usuario)
);

-- Tabla de Transferencias entre Almacenes  
CREATE TABLE Transferencias (
    id_transferencia BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    id_material BIGINT UNSIGNED,
    id_producto BIGINT UNSIGNED,
    cantidad INT NOT NULL,
    fecha_transferencia TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    id_ubicacion_origen BIGINT UNSIGNED,
    id_ubicacion_destino BIGINT UNSIGNED,
    id_usuario BIGINT UNSIGNED,
    FOREIGN KEY (id_material) REFERENCES Materiales(id_material),
    FOREIGN KEY (id_producto) REFERENCES ProductosTerminados(id_producto),
    FOREIGN KEY (id_ubicacion_origen) REFERENCES Ubicaciones(id_ubicacion),
    FOREIGN KEY (id_ubicacion_destino) REFERENCES Ubicaciones(id_ubicacion),
    FOREIGN KEY (id_usuario) REFERENCES Usuarios(id_usuario)
);

-- Tabla de Ajustes de Inventario  
CREATE TABLE AjustesInventario (
    id_ajuste BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    id_material BIGINT UNSIGNED,
    id_producto BIGINT UNSIGNED,
    cantidad INT NOT NULL,
    fecha_ajuste TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    motivo VARCHAR(100),
    id_usuario BIGINT UNSIGNED,
    FOREIGN KEY (id_material) REFERENCES Materiales(id_material),
    FOREIGN KEY (id_producto) REFERENCES ProductosTerminados(id_producto),
    FOREIGN KEY (id_usuario) REFERENCES Usuarios(id_usuario)
);

-- Tabla de Historial de Movimientos  
CREATE TABLE HistorialMovimientos (
    id_movimiento BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    id_material BIGINT UNSIGNED,
    id_producto BIGINT UNSIGNED,
    tipo_movimiento VARCHAR(50) CHECK (tipo_movimiento IN ('Entrada', 'Salida', 'Transferencia', 'Ajuste')),
    cantidad INT NOT NULL,
    fecha_movimiento TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    id_usuario BIGINT UNSIGNED,
    FOREIGN KEY (id_material) REFERENCES Materiales(id_material),
    FOREIGN KEY (id_producto) REFERENCES ProductosTerminados(id_producto),
    FOREIGN KEY (id_usuario) REFERENCES Usuarios(id_usuario)
);

-- Tabla de Facturas 
CREATE TABLE Facturas (
    id_factura BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    numero_factura VARCHAR(50) UNIQUE NOT NULL,
    id_proveedor BIGINT UNSIGNED,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_proveedor) REFERENCES Proveedores(id_proveedor)
);

-- Tabla de DetallesFactura 
CREATE TABLE DetallesFactura (
    id_detalle BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    id_factura BIGINT UNSIGNED,
    id_material BIGINT UNSIGNED,
    cantidad INT NOT NULL,
    FOREIGN KEY (id_factura) REFERENCES Facturas(id_factura),
    FOREIGN KEY (id_material) REFERENCES Materiales(id_material)
);

-- Tabla de Inspecciones 
CREATE TABLE Inspecciones (
    id_inspeccion BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    id_material BIGINT UNSIGNED,
    id_proveedor BIGINT UNSIGNED,
    resultado VARCHAR(100) CHECK (resultado IN ('Aprobado', 'Rechazado')),
    observaciones TEXT,
    fecha_inspeccion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_material) REFERENCES Materiales(id_material),
    FOREIGN KEY (id_proveedor) REFERENCES Proveedores(id_proveedor)
);