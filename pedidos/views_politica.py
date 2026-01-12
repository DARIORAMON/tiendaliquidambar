from django.views.generic import View
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from usuario.models import Perfil
from django.contrib.sites.models import Site

class PaginaPolitica(View):
    template = "pedidos/politica.html"

    def get(self, request):
        params = {}
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

        return render(request, self.template, params)