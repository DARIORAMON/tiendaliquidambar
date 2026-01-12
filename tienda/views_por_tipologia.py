from django.shortcuts import render
from django.shortcuts import redirect
from productos.models.categoria import Categoria
from productos.models.categoria import Menu
from productos.models.categoria import TalleCatagoria
from productos.models.categoria import TipologiaCatagoria
from django.contrib.auth.models import User
import json
from django.http import HttpResponse

# from .models.cliente import Cliente
from productos.models.producto import ImagenProducto
from productos.models.producto import Producto
from productos.models.producto import ProductoAsociado
from productos.models.producto import CadaProducto
from productos.models.producto import ColorProducto
from productos.models.producto import CuidadoProducto
from productos.models.producto import TalleProducto
from django.db.models import Q
from django.views.generic import View
from django.http import HttpResponseRedirect
from .menu import crear_menu
from usuario.models import ClaveMayorista
from django.contrib.sites.models import Site
from presentacion.models import TiendaCarrouselle


class PorTipologia(View):
    template = "tienda/tienda.html"

    def get(self, request, categoria_slug, tipologia_nombre):
        params = {}

        tienda_carrouselle = TiendaCarrouselle.objects.filter()
        params["tienda_carrouselle"] = tienda_carrouselle
        categorias = Categoria.get_all_categorias()
        la_categoria = Categoria.objects.get(slug=categoria_slug)
        datos_menu = Menu.objects.filter(
            Q(estado="Publicado"),
            ~Q(stock=0),
            ~Q(peso=0.00),
            ~Q(precio=0.00),
            #~Q(precio_mayorista=0.00),
        )
        # ##########################################################
        # CREANDO MENÚ
        # ##########################################################
        elementos_menu = crear_menu(datos_menu)
        #print(elementos_menu["diamond"])
        # ################ FIN CREAR MENÚ ##########################
        imagenes = ImagenProducto.objects.all()
        talle = TalleCatagoria.objects.all()
        talles = TalleProducto.objects.all()
        colores = ColorProducto.objects.all()
        cuidados = CuidadoProducto.objects.all()
        tipologia = TipologiaCatagoria.objects.all()
        producto_asociado = ProductoAsociado.objects.all()
        # cada_producto = CadaProducto.objects.all()
        # productos = Producto.objects.filter(Q(estado="Publicado"), Q(tipologia=tipologia_nombre))

        cada_producto = CadaProducto.objects.filter(
            Q(estado="Publicado"),
            ~Q(stock=0),
            ~Q(peso=0.00),
            ~Q(precio=0.00),
            #~Q(precio_mayorista=0.00),
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
            Q(tipologia=tipologia_nombre),
            Q(articulo__in=cada_p_lista2),
        )
        
        # ##########################################################
        # PARA OBTENER TALLES y COLORES
        # ###########################################################
        cada_talle_color = CadaProducto.objects.filter(
            Q(estado="Publicado"),
            ~Q(stock=0),
            ~Q(peso=0.00),
            ~Q(precio=0.00),
            #~Q(precio_mayorista=0.00),
        )
        cada_el_talle = []
        cada_el_color = []
        for cada in cada_talle_color:
            #print(cada.talle)
            cada_el_talle.append(cada.talle)
            try:
                valor_c = ColorProducto.objects.get(nombre=cada.color)
                cada_el_color.append((valor_c.nombre, valor_c.hexadecimal))
            except:
                print("problema color")
        cada_el_talle = set(cada_el_talle) 
        cada_el_talle = list(cada_el_talle) 
        cada_el_talle = sorted(cada_el_talle)
        cada_el_color = set(cada_el_color) 
        cada_el_color = list(cada_el_color)    
        #print(cada_el_talle, cada_el_color)
        
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
        # ##########################################################
        # PARA MAYORISTA
        # ###########################################################
        usuario = request.user
        clave_mayorista = ClaveMayorista.objects.last()
        params["clave_mayorista"] = clave_mayorista.clave
        try:
            clave_mayorista_usuario = DatosUsuario.objects.get(usuario=usuario)
            params["clave_mayorista_usuario"] = clave_mayorista_usuario.clave
        except:
            print("Usuario no registrado")
            # params["clave_mayorista_usuario"] = "alfjderet335n353gg353n3AWL355535me00911HYL"
        # ############################################################
        params["nombre_sitio"] = "Prestige"
        params["categorias"] = categorias
        params["elementos_menu"] = elementos_menu
        params["talle"] = talle
        params["talles"] = talles
        params["tipologia"] = tipologia
        params["productos"] = productos
        params["imagenes"] = imagenes
        params["cuidados"] = cuidados
        params["colores"] = colores
        params["cada_producto"] = cada_producto
        params["ruta_en_tienda_categoria"] = la_categoria
        params["ruta_en_tienda_tipologia"] = tipologia_nombre
        params["producto_asociado"] = producto_asociado
        params["cada_el_talle"] = cada_el_talle
        params["cada_el_color"] = cada_el_color
        try:
            params["usuario"] = request.user
        except:
            print("---------  No estás logueado ")
        return render(request, self.template, params)
