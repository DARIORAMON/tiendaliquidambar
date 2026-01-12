from django.urls import path
from tienda import crear_datos_localstorage
from tienda import views_agregar
from tienda import views_agregar_i
from tienda.views_tienda import Tienda, TiendaBusqueda 
from tienda.views_por_categoria import PorCategoria
from tienda import views_comprar
from tienda import views_quitar
from tienda.views_ver_producto import VerProducto


urlpatterns = [
    path("agregar/", views_agregar.agregar, name="agregar"),
    path("agregar_i/", views_agregar_i.agregar_i, name="agregar_i"),
    path("", Tienda.as_view(), name="tienda"),
    path("tienda_busqueda/<buscar>/", TiendaBusqueda.as_view(), name="tienda_busqueda"),
    path("categoria/<categoria_slug>/", PorCategoria.as_view(), name="categoria"),
    path("comprar/", views_comprar.comprar, name="comprar"),
    path("ver_producto/<articulo>/", VerProducto.as_view(), name="ver_producto"),
    path("quitar/", views_quitar.quitar, name="quitar"),
    path(
        "crear_localstorage/",
        crear_datos_localstorage.crear_localstorage,
        name="crear_localstorage",
    ),
   
]

