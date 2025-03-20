from rest_framework.response import Response
import uuid
from django.contrib.sessions.models import Session
from django.contrib.sessions.backends.db import SessionStore
from rest_framework import status
from django.contrib.auth import authenticate
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import viewsets
from .models import (
    Usuarios, Proveedores, Materiales, ProductosTerminados, OrdenesProduccion,
    AsignacionMateriales, Ubicaciones, UbicacionStock, Entradas, Salidas,
    Inventario, Mermas, Notificaciones, Transferencias, AjustesInventario,
    HistorialMovimientos, Facturas, DetallesFactura, Inspecciones
)
from .serializers import (
    UsuariosSerializer, ProveedoresSerializer, MaterialesSerializer,
    ProductosTerminadosSerializer, OrdenesProduccionSerializer,
    AsignacionMaterialesSerializer, UbicacionesSerializer, UbicacionStockSerializer,
    EntradasSerializer, SalidasSerializer, InventarioSerializer, MermasSerializer,
    NotificacionesSerializer, TransferenciasSerializer, AjustesInventarioSerializer,
    HistorialMovimientosSerializer, FacturasSerializer, DetallesFacturaSerializer,
    InspeccionesSerializer, RegisterSerializer, LoginSerializer
)


##A ESTO ME REFERIA COMO CAGADERO, QUIZAS HACER UN ARCHIVO POR VISTA SERIA MAS MODULAR Y PRACTICO PERO LA NETA Q WEBA


#OKEY ESTAS SON LAS VIEWS CLASICAS SON SOLO UN SELECT A LA TABLA Y YA, PARA LAS FUNCIONALIDADES SE AGREGA UN VIEW ESPECIFICO




##VISTA REGISTRO
class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            usuario = serializer.save()
            return Response(
                {
                    "message": "Usuario registrado con éxito",
                    "usuario": {
                        "id_usuario": usuario.id_usuario,
                        "nombre": usuario.nombre,
                        "correo": usuario.correo,
                        "Contrasena": usuario.contraseña,
                        "rol": usuario.rol,
                        "activo": usuario.activo
                    }
                },
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#VISTA PARA LOGIN
class LoginView(APIView):
    def post(self, request):
        data = request.data
        correo = data.get("correo")
        contraseña = data.get("contraseña")

        try:
            usuario = Usuarios.objects.get(correo=correo)

            if usuario and usuario.contraseña == contraseña:
              
                request.session["usuario_id"] = usuario.id_usuario
                request.session.save()  

                print("SESION GUARDADA:", request.session.items()) 

                response = Response({
                    "mensaje": "Login exitoso",
                    "usuario": {
                        "id_usuario": usuario.id_usuario,
                        "nombre": usuario.nombre,
                        "correo": usuario.correo,
                        "rol": usuario.rol,
                    
                    }
                })

                # Configurar la cookie de sesión
                response.set_cookie(
                    key="sessionid",
                    value=request.session.session_key,
                    httponly=True, 
                    secure=True, 
                    samesite="Lax"
                )

                return response
            else:
                return Response({"error": "Credenciales inválidas"}, status=status.HTTP_401_UNAUTHORIZED)

        except Usuarios.DoesNotExist:
            return Response({"error": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        

        

class LogoutView(APIView):
    def post(self, request):
        request.session.flush()  
        response = Response({"mensaje": "Sesión cerrada"}, status=status.HTTP_200_OK)
        response.delete_cookie("sessionid")  
        return response



class UsuarioInfoView(APIView):
    def get(self, request):
        print("🔍 SESION ACTUAL:", request.session.items())  

        usuario_id = request.session.get("usuario_id")

        if not usuario_id:
            return Response({"error": "No autenticado"}, status=status.HTTP_401_UNAUTHORIZED)

        try:
            usuario = Usuarios.objects.get(id_usuario=usuario_id)
      
            imagen_perfil_url = (
                request.build_absolute_uri(usuario.imagen_perfil.url)
                if usuario.imagen_perfil
                else None
            )

            return Response({
                "id_usuario": usuario.id_usuario,
                "nombre": usuario.nombre,
                "correo": usuario.correo,
                "rol": usuario.rol,
                "imagen_perfil": imagen_perfil_url,  
            })
        except Usuarios.DoesNotExist:
            return Response({"error": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)

##ESTAS 2 VISTAS SON LAS QUE SE ENCARGAN JUNTO CON SUS SERIALIZERS DE EL PROCESO DEL LOGIN
##SE PREGUNTARAN PORQUE ESTAS VISTAS SON API VIEW Y NO MODELVIEWSET COMO LAS OTRAS
##APIView se usa en Login y Register porque estas operaciones no están directamente relacionadas con el modelo como CRUD básico  



##VISTAS PARA TABLAS

# Vista para Usuarios
class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = Usuarios.objects.all()
    serializer_class = UsuariosSerializer

# Vista para Proveedores
class ProveedoresViewSet(viewsets.ModelViewSet):
    queryset = Proveedores.objects.all()
    serializer_class = ProveedoresSerializer

# Vista para Materiales
class MaterialesViewSet(viewsets.ModelViewSet):
    queryset = Materiales.objects.all()
    serializer_class = MaterialesSerializer

# Vista para ProductosTerminados
class ProductosTerminadosViewSet(viewsets.ModelViewSet):
    queryset = ProductosTerminados.objects.all()
    serializer_class = ProductosTerminadosSerializer

# Vista para OrdenesProduccion
class OrdenesProduccionViewSet(viewsets.ModelViewSet):
    queryset = OrdenesProduccion.objects.all()
    serializer_class = OrdenesProduccionSerializer

# Vista para AsignacionMateriales
class AsignacionMaterialesViewSet(viewsets.ModelViewSet):
    queryset = AsignacionMateriales.objects.all()
    serializer_class = AsignacionMaterialesSerializer

# Vista para Ubicaciones
class UbicacionesViewSet(viewsets.ModelViewSet):
    queryset = Ubicaciones.objects.all()
    serializer_class = UbicacionesSerializer

# Vista para UbicacionStock
class UbicacionStockViewSet(viewsets.ModelViewSet):
    queryset = UbicacionStock.objects.all()
    serializer_class = UbicacionStockSerializer

# Vista para Entradas
class EntradasViewSet(viewsets.ModelViewSet):
    queryset = Entradas.objects.all()
    serializer_class = EntradasSerializer

# Vista para Salidas
class SalidasViewSet(viewsets.ModelViewSet):
    queryset = Salidas.objects.all()
    serializer_class = SalidasSerializer

# Vista para Inventario
class InventarioViewSet(viewsets.ModelViewSet):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer

# Vista para Mermas
class MermasViewSet(viewsets.ModelViewSet):
    queryset = Mermas.objects.all()
    serializer_class = MermasSerializer

# Vista para Notificaciones
class NotificacionesViewSet(viewsets.ModelViewSet):
    queryset = Notificaciones.objects.all()
    serializer_class = NotificacionesSerializer

# Vista para Transferencias
class TransferenciasViewSet(viewsets.ModelViewSet):
    queryset = Transferencias.objects.all()
    serializer_class = TransferenciasSerializer

# Vista para AjustesInventario
class AjustesInventarioViewSet(viewsets.ModelViewSet):
    queryset = AjustesInventario.objects.all()
    serializer_class = AjustesInventarioSerializer

# Vista para HistorialMovimientos
class HistorialMovimientosViewSet(viewsets.ModelViewSet):
    queryset = HistorialMovimientos.objects.all()
    serializer_class = HistorialMovimientosSerializer

# Vista para Facturas
class FacturasViewSet(viewsets.ModelViewSet):
    queryset = Facturas.objects.all()
    serializer_class = FacturasSerializer

# Vista para DetallesFactura
class DetallesFacturaViewSet(viewsets.ModelViewSet):
    queryset = DetallesFactura.objects.all()
    serializer_class = DetallesFacturaSerializer

# Vista para Inspecciones
class InspeccionesViewSet(viewsets.ModelViewSet):
    queryset = Inspecciones.objects.all()
    serializer_class = InspeccionesSerializer