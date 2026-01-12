from django.shortcuts import render
from productos.models.categoria import Categoria
from productos.models.producto import ImagenProducto
from productos.models.producto import Producto
from django.db.models import Q
from django.views.generic import View
from usuario.models import Perfil
from django.contrib.sites.models import Site


class Tienda(View):
    template = "tienda/tienda.html"

    def get(self, request):
        params = {}
        categorias = Categoria.get_all_categorias()

        # ################ FIN CREAR MENÚ ##########################
        imagenes = ImagenProducto.objects.all()
        # cada_producto = CadaProducto.objects.all()
        cada_producto = Producto.objects.filter(
            Q(estado="Publicado"),
            ~Q(stock=0),
            ~Q(peso=0.00),
            ~Q(precio=0.00),
            #~Q(precio_mayorista=0.00),
        )
        cada_p_lista = []
        for cada in cada_producto:
            cada_p_lista.append(cada.articulo)
        # print(cada_p_lista)
        cada_p_set = set(cada_p_lista)
        # print(cada_p_set)
        cada_p_lista2 = list(cada_p_set)
        # print(cada_p_lista2)
        # chequeo_stock_lista = []
        productos = Producto.objects.filter(
            Q(estado="Publicado"), Q(articulo__in=cada_p_lista2)
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
        current_site = Site.objects.get_current()
        params["dominio_actual"] = current_site.domain
        params["nombre_sitio"] = "Prestige"
        params["categorias"] = categorias
        params["productos"] = productos
        params["imagenes"] = imagenes
        params["cada_producto"] = cada_producto
        params["lo_que_veo"] = "2"
        try:
            params["usuario"] = request.user
        except:
            print("---------  No estás logueado ")
        return render(request, self.template, params)


class TiendaBusqueda(View):
    template = "tienda/tienda.html"

    def get(self, request, buscar):
        params = {}
        categorias = Categoria.get_all_categorias()
        imagenes = ImagenProducto.objects.all()
        buscar = buscar.replace("%20", " ")
        # cada_producto = CadaProducto.objects.all()
        cada_producto = Producto.objects.filter(
            Q(estado="Publicado"),
            ~Q(stock=0),
            ~Q(peso=0.00),
            ~Q(precio=0.00),
            Q(articulo__icontains=buscar)
            | Q(name__icontains=buscar)
        )
        if cada_producto.exists():
            lo_que_veo = "1"
        else:
            lo_que_veo = "0"
        cada_producto2 = list(cada_producto)
        valor_cantidad = len(cada_producto2)
        cada_p_lista = []
        for cada in cada_producto:
            cada_p_lista.append(cada.articulo)
        cada_p_set = set(cada_p_lista)
        cada_p_lista2 = list(cada_p_set)
        productos = Producto.objects.filter(
            Q(estado="Publicado"), Q(articulo__in=cada_p_lista2)
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
        current_site = Site.objects.get_current()
        params["dominio_actual"] = current_site.domain
        params["nombre_sitio"] = "Prestige"
        params["categorias"] = categorias
        params["productos"] = productos
        params["imagenes"] = imagenes
        params["cada_producto"] = cada_producto
        params["lo_que_veo"] = lo_que_veo
        try:
            params["usuario"] = request.user
        except:
            print("---------  No estás logueado ")
        return render(request, self.template, params)
def error_404_view(request, exception):
    return render(request, "400.html")
