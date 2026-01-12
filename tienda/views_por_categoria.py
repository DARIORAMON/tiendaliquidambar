from django.shortcuts import render
from productos.models.categoria import Categoria
from productos.models.producto import ImagenProducto
from productos.models.producto import Producto
from django.db.models import Q
from django.views.generic import View
from django.contrib.sites.models import Site



class PorCategoria(View):
    template = "tienda/tienda.html"

    def get(self, request, categoria_slug):
        params = {}
        categorias = Categoria.get_all_categorias()

        la_categoria = Categoria.objects.get(slug=categoria_slug)
        print(la_categoria)
        imagenes = ImagenProducto.objects.all()
        cada_producto = Producto.objects.filter(
            Q(estado="Publicado"),
            ~Q(stock=0),
            ~Q(peso=0.00),
            ~Q(precio=0.00),
        )
        cada_p_lista = []
        for cada in cada_producto:
            cada_p_lista.append(cada.articulo)
        print(cada_p_lista)
        cada_p_set = set(cada_p_lista)
        print(cada_p_set)
        cada_p_lista2 = list(cada_p_set)
        print(cada_p_lista2)
        # chequeo_stock_lista = []
        categoria_id = Categoria.objects.get(slug=categoria_slug)
        productos = Producto.objects.filter(
            Q(estado="Publicado"),
            Q(categoria=categoria_id),
            Q(articulo__in=cada_p_lista2),
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
        params["tipologia"] = tipologia
        params["productos"] = productos
        params["imagenes"] = imagenes
        params["cada_producto"] = cada_producto
        params["ruta_en_tienda_categoria"] = la_categoria
        params["ruta_en_tienda_categoria_id"] = la_categoria.id
        try:
            params["usuario"] = request.user
        except:
            print("---------  No estás logueado ")
        return render(request, self.template, params)
