from productos.models.producto import Producto
from django.views.generic import View
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.db.models import Q
from usuario.models import Perfil
from django.contrib.sites.models import Site
from .models import ConfiguracionEnvio
import requests
from geopy.distance import geodesic
from django.conf import settings
import logging
from django.db.models import Sum

logger = logging.getLogger(__name__)

class Carrito(View):
    template = "carro/carrito.html"

    def get(self, request):
        params = {}   
        carro = request.session.get("carro", {})
        ids = list(carro.keys())
        ids2 = []

        for id in ids:
            if id.startswith("prestige"):
                try:
                    val = int(id.split("_")[1])
                    ids2.append(val)
                except (ValueError, IndexError):
                    continue

        art_venta = Producto.objects.filter(pk__in=ids2)
        params["los_productos"] = art_venta

        if request.user.is_authenticated:
            params["usuario"] = request.user
            try:
                datos_para_imagen = Perfil.objects.get(usuario=request.user.pk)
                params["datos_para_imagen"] = datos_para_imagen
            except ObjectDoesNotExist:
                pass

        try:
            current_site = Site.objects.get_current()
            params["dominio_actual"] = current_site.domain
        except:
            params["dominio_actual"] = "localhost"

        costo_envio = request.session.get('costo_envio', 0)
        params["costo_envio"] = costo_envio

        return render(request, self.template, params)

    def post(self, request):
        codigo_postal_cliente = request.POST.get('codigo_postal')
        config_envio = ConfiguracionEnvio.objects.first()

        if config_envio and codigo_postal_cliente:
            try:
                coords_base = self.obtener_coordenadas(config_envio.codigo_postal_base)
                coords_cliente = self.obtener_coordenadas(codigo_postal_cliente)

                if coords_base and coords_cliente:
                    distancia_km = geodesic(coords_base, coords_cliente).kilometers

                    if distancia_km > 60:
                        request.session['costo_envio'] = "Para distancias mayores a 60 km coordinar con el vendedor el envío por encomienda y transporte a convenir, una vez finalizada la compra."
                    else:
                        costo_envio = distancia_km * float(config_envio.tarifa_por_km)
                        request.session['costo_envio'] = round(costo_envio, 2)
                    
                    request.session['error_mensaje'] = None
                else:
                    request.session['error_mensaje'] = "No se pudieron obtener las coordenadas."

            except Exception as e:
                logger.error(f"Error calculando el costo de envío: {e}")
                request.session['costo_envio'] = None
                request.session['error_mensaje'] = "Error al calcular el envío. Intente de nuevo."
        else:
            request.session['error_mensaje'] = "Faltan datos de configuración o código postal."

        return self.get(request)

    def obtener_coordenadas(self, codigo_postal):
        """
        Función para obtener las coordenadas (latitud, longitud) desde un código postal utilizando OpenCage API.
        """
        try:
            api_key = getattr(settings, 'OPENCAGE_API_KEY', '')
            if not api_key:
                return None
                
            api_url = f"https://api.opencagedata.com/geocode/v1/json?q={codigo_postal},Argentina&key={api_key}"
            response = requests.get(api_url, timeout=5)

            if response.status_code == 200:
                data = response.json()
                if data.get('results') and len(data['results']) > 0:
                    lat = data['results'][0]['geometry']['lat']
                    lng = data['results'][0]['geometry']['lng']
                    return (lat, lng)
            return None
        except Exception as e:
            logger.error(f"Error en OpenCage: {e}")
            return None
