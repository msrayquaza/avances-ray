from rest_framework import serializers
from .models import (
    Usuarios, Proveedores, Materiales, ProductosTerminados, OrdenesProduccion,
    AsignacionMateriales, Ubicaciones, UbicacionStock, Entradas, Salidas,
    Inventario, Mermas, Notificaciones, Transferencias, AjustesInventario,
    HistorialMovimientos, Facturas, DetallesFactura, Inspecciones
)
from django.contrib.auth.hashers import make_password



##SERIALIZERS LOGIN
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = ['user_id','id_usuario', 'nombre', 'correo', 'contraseña', 'rol', 'activo']
        extra_kwargs = {'contraseña': {'write_only': True}}


class LoginSerializer(serializers.Serializer):
    correo = serializers.EmailField()
    contraseña = serializers.CharField(write_only=True)



#SERIALIZERS TABLAS

class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = [
            'id_usuario', 'nombre', 'correo', 'contraseña', 'rol',
            'activo', 'fecha_registro', 'imagen_perfil'
        ]

class ProveedoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedores
        fields = '__all__'

class MaterialesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materiales
        fields = '__all__'

class ProductosTerminadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductosTerminados
        fields = '__all__'

class OrdenesProduccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdenesProduccion
        fields = '__all__'

class AsignacionMaterialesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AsignacionMateriales
        fields = '__all__'

class UbicacionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ubicaciones
        fields = '__all__'

class UbicacionStockSerializer(serializers.ModelSerializer):
    class Meta:
        model = UbicacionStock
        fields = '__all__'

class EntradasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entradas
        fields = '__all__'

class SalidasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salidas
        fields = '__all__'

class InventarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventario
        fields = '__all__'

class MermasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mermas
        fields = '__all__'

class NotificacionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notificaciones
        fields = '__all__'

class TransferenciasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transferencias
        fields = '__all__'

class AjustesInventarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = AjustesInventario
        fields = '__all__'

class HistorialMovimientosSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistorialMovimientos
        fields = '__all__'

class FacturasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facturas
        fields = '__all__'

class DetallesFacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetallesFactura
        fields = '__all__'

class InspeccionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inspecciones
        fields = '__all__'