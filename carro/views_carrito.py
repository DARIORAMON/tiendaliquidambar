from productos.models.producto import Producto
from django.views.generic import View
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.db.models import Q
from usuario.models import Perfil
from django.contrib.sites.models import Site
from .models import ConfiguracionEnvio  # Importamos el modelo de configuración de envío
import requests
from geopy.distance import geodesic  # Librería para calcular distancia geográfica
from django.conf import settings  # Para acceder a las variables de configuración de la API
import logging
from django.db.models import Sum

class Carrito(View):
    template = "carro/carrito.html"

    def get(self, request):
        params = {}   
        ids = list(request.session.get("carro").keys())
        ids2 = []

        for id in ids:
            print(id[:8])
            if id[:8] == "prestige":
                val = id[9:]
                val = int(val)
                ids2.append(val)     
 
        # ##########################################################
        # PARA USUARIO
        # ###########################################################
        # user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        # ##########################################################
        # PARA USUARIO
        # ###########################################################
        art_venta = Producto.objects.filter(pk__in=ids2)
        print(art_venta)
        params["los_productos"] = art_venta
   
          

        # ##########################################################
        # PARA USUARIO
        # ###########################################################
        if request.user.is_authenticated:
            params["usuario"] = request.user
            try:
                datos_para_imagen = Perfil.objects.get(usuario=request.user.pk)
                params["datos_para_imagen"] = datos_para_imagen
            except ObjectDoesNotExist:
                pass
        # ##########################################################
        # PARA RUTAS EN LINKS
        # ###########################################################
        current_site = Site.objects.get_current()
        params["dominio_actual"] = current_site.domain

        # Cargar el costo de envío de la sesión si existe
        costo_envio = request.session.get('costo_envio', 0)
        params["costo_envio"] = costo_envio
 



        return render(request, self.template, params)
    



    
    def post(self, request):
        # Obtener el código postal ingresado por el cliente
        codigo_postal_cliente = request.POST.get('codigo_postal')

        # Obtener la configuración de envío desde el panel de administración
        try:
            config_envio = ConfiguracionEnvio.objects.first()  # Asumimos que solo hay una configuración
        except ConfiguracionEnvio.DoesNotExist:
            config_envio = None

        if config_envio and codigo_postal_cliente:
            # Calcular la distancia entre el código postal base y el ingresado
            try:
                coords_base = self.obtener_coordenadas(config_envio.codigo_postal_base)
                coords_cliente = self.obtener_coordenadas(codigo_postal_cliente)

                # Calcular la distancia en kilómetros
                distancia_km = geodesic(coords_base, coords_cliente).kilometers

                # Verificar si la distancia es mayor a 60 km
                if distancia_km > 60:
                    request.session['costo_envio'] = "Para distancias mayores a 60 km coordinar con el vendedor el envío por encomienda y transporte a convenir, una vez finalizada la compra."
                else:
                    # Calcular el costo de envío en base a la tarifa por kilómetro
                    costo_envio = distancia_km * float(config_envio.tarifa_por_km)
                    request.session['costo_envio'] = round(costo_envio, 2)

                # Resetear el mensaje de error si el cálculo fue exitoso
                request.session['error_mensaje'] = None

            except Exception as e:
                print(f"Error calculando el costo de envío: {e}")
                request.session['costo_envio'] = None
                request.session['error_mensaje'] = "No se pudo encontrar el código postal ingresado. Por favor, verifica e intenta de nuevo."
        else:
            request.session['costo_envio'] = "Configuración de envío no encontrada."
            request.session['error_mensaje'] = "No se pudo encontrar la configuración de envío."

        # Redirigir nuevamente al carrito de compras
        return self.get(request)

    def obtener_coordenadas(self, codigo_postal):
        """
        Función para obtener las coordenadas (latitud, longitud) desde un código postal.
        """
        api_url = f"https://api.opencagedata.com/geocode/v1/json?q={codigo_postal},Argentina&key={settings.OPENCAGE_API_KEY}"
        response = requests.get(api_url)

        if response.status_code == 200:
            data = response.json()
            if data.get('postalCodes'):
                lat = data['postalCodes'][0]['lat']
                lng = data['postalCodes'][0]['lng']
                return (lat, lng)
            else:
                print(f"No se encontraron coordenadas para el código postal: {codigo_postal}")
                raise Exception(f"No se encontraron coordenadas para el código postal {codigo_postal}.")
        else:
            raise Exception(f"Error en la solicitud a GeoNames. Código de estado: {response.status_code}")
        
    #response = requests.get("https://api.opencagedata.com/geocode/v1/json?q={codigo_postal},Argentina&key={settings.OPENCAGE_API_KEY}")
    print(response.json())  # Para ver exactamente qué datos está devolviendo la API


    logger = logging.getLogger(__name__)

    def obtener_coordenadas(self, codigo_postal):
        """
        Función para obtener las coordenadas (latitud, longitud) desde un código postal utilizando OpenCage API.
        """
        api_url = f"https://api.opencagedata.com/geocode/v1/json?q={codigo_postal},Argentina&key={settings.OPENCAGE_API_KEY}"
        
        response = requests.get(api_url)

        if response.status_code == 200:
            data = response.json()
            if data['results']:
                lat = data['results'][0]['geometry']['lat']
                lng = data['results'][0]['geometry']['lng']
                return (lat, lng)
        raise Exception("No se pudieron obtener las coordenadas del código postal.")
