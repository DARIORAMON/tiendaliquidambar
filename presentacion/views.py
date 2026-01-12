from django.shortcuts import render
from productos.models.categoria import Categoria
from productos.models.producto import ImagenProducto
from productos.models.producto import Producto
from django.db.models import Q
from django.views.generic import View
from django.http import HttpResponseRedirect
from django.contrib.sites.models import Site
from django.shortcuts import render
from contacto.models import Consulta
from contacto.forms import ConsultaForm
from presentacion.models import CarrouselIntroduccion
from presentacion.models import ProductosDestacados
from presentacion.models import AireLibre
from presentacion.models import AireLibreBeneficios
from presentacion.models import Temporada
from presentacion.models import PreguntasFrecuentes

class Index(View):
    template = "presentacion/index.html"
    def get(self, request):
        form = ConsultaForm()
        params = {}
        params["form"] = form
        usuario = request.user

        carrou_intro = CarrouselIntroduccion.objects.filter()
        params["carrou_intro"] = carrou_intro

        prod_dest_intro = ProductosDestacados.objects.filter()
        params["prod_dest_intro"] = prod_dest_intro

        try:
            aire_libre_intro = AireLibre.objects.latest("id")
            aire_libreb_intro = AireLibreBeneficios.objects.filter(
                Q(beneficio=aire_libre_intro)
            )
            params["aire_libre_intro"] = aire_libre_intro
            params["aire_libreb_intro"] = aire_libreb_intro
        except:
            print("---------  Aún no se ha cargado Aire Libre ")

        try:
            temporada_intro = Temporada.objects.latest("id")
            params["temporada_intro"] = temporada_intro
        except:
            print("---------  Aún no se ha cargado Temporada ")

        try:
            params["usuario"] = request.user
        except:
            print("---------  No estás logueado ")
        categorias = Categoria.get_all_categorias()


        imagenes = ImagenProducto.objects.all()

        productos = Producto.objects.filter(
            Q(estado="Publicado")
        )
        # ##########################################################
        # PARA INICIALIZAR LA VARIABLE DE SESSION CARRO
        # ###########################################################
        try:
            request.session["carro"]
        except:
            request.session["carro"] = {}
        # ##########################################################
        # PARA RUTAS EN LINKS
        # ###########################################################
        try:   
            current_site = Site.objects.get_current()
            params["dominio_actual"] = current_site.domain
        except:
            print("--- no hay current site") 
        # ############################################################
        params["nombre_sitio"] = "Prestige"
        params["categorias"] = categorias
        params["productos"] = productos
        params["imagenes"] = imagenes

        try:
            params["usuario"] = request.user
        except:
            print("---------  No estás logueado ")
        return render(request, self.template, params)

    def post(self, request):
        form = ConsultaForm(request.POST or None)
        if form.is_valid():
            for key in form.cleaned_data:
                print(key)

            nombre = form.cleaned_data["nombre"]
            descripcion = form.cleaned_data["descripcion"]
            mail = form.cleaned_data["mail"]
            estado_respuesta = form.cleaned_data["estado_respuesta"]
            telefono = form.cleaned_data["telefono"]
            fecha = form.cleaned_data["fecha"]
            com = Consulta(
                nombre=nombre,
                descripcion=descripcion,
                mail=mail,
                estado_respuesta="No Contestada",
                telefono=telefono,
                fecha=fecha,
            )
            com.save()
        else:
            print("")
        return HttpResponseRedirect("/contacto/mensaje_enviado")

class PreguntasFrecuentesVista(View):
    template = "presentacion/preguntas_frecuentes.html"

    def get(self, request):
        params = {}
        preguntas = PreguntasFrecuentes.objects.all()
        params["preguntas"]=preguntas
        return render(request, self.template, params)
 