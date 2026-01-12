from django.shortcuts import render
from productos.models.categoria import Categoria
from productos.models.producto import ImagenProducto
from productos.models.producto import Producto
from django.db.models import Q
from django.views.generic import View
from django.contrib.sites.models import Site


class VerProducto(View):
    template = "tienda/ver_producto.html"

    def get(self, request, articulo):
        params = {}
        categorias = Categoria.get_all_categorias()
 
        # ##########################################################
        # CREANDO MENÚ
        # ##########################################################
        # ################ FIN CREAR MENÚ ##########################
        imagenes = ImagenProducto.objects.all()
 
        cada_producto = Producto.objects.filter(
            Q(estado="Publicado"), 
            ~Q(stock=0), 
            ~Q(peso=0.00), 
            ~Q(precio=0.00), 
            Q(articulo=articulo)
        )
        cada_p_lista = []
        for cada in cada_producto:
            cada_p_lista.append(cada.articulo)
        cada_p_set = set(cada_p_lista)
        cada_p_lista2 = list(cada_p_set)

        producto = Producto.objects.get(Q(estado="Publicado"), Q(articulo=articulo))
        usuario = request.user

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
        params["producto"] = producto
        params["imagenes"] = imagenes
        params["cada_producto"] = cada_producto
        try:
            params["usuario"] = request.user
        except:
            print("---------  No estás logueado ")
        return render(request, self.template, params)