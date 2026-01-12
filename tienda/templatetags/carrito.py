from django import template
from productos.models.producto import Producto
from django.db.models import Q

register = template.Library()


@register.filter(name="is_in_carro")
def is_in_carro(producto, carro):

    keys = carro.keys()
    for id in keys:
        if int(id) == producto.id:
            return True
    # print(keys)
    # print("*********** En templatetags carrito *************")
    # print(producto, carro)
    return False


@register.filter(name="carro_cantida")
def carro_cantida(producto, carro):

    keys = carro.keys()
    for id in keys:
        #print("AAAAAAAAAAAAAA")
        #print(id)
        prod = "prestige_" + str(producto.id)
        if id == prod:
            #print("AAAAA2AAAA")
            #print(carro.get(id))
            return carro.get(id)
    """
    keys = carro.keys()
    for id in keys:
        if int(id) == producto.id:
            return carro.get(id)
    """
    return 0


# *************************************************************************
# * TOMAR PRECIOS PARCIALES
# *************************************************************************
@register.filter(name="precio_total_producto")
def precio_total_producto(producto, carro):
    valor = int(carro_cantida(producto, carro)) * (
        producto.precio - ((producto.precio * producto.descuento) / 100)
    )
    valor = "{0:.1f}".format(valor)
    return float(valor)


@register.filter(name="precio_total_producto_mayorista")
def precio_total_producto_mayorista(producto, carro):
    #print("jjjjjjjjjjjj")
    #print(int(carro_cantida(producto, carro)))
    #print(producto.precio_mayorista)
    #print(producto.descuento_mayorista)
    #print(((producto.precio_mayorista * producto.descuento_mayorista) / 100))
    #print("jjjjj22222222jjjj")
    valor = int(carro_cantida(producto, carro)) * (
        producto.precio_mayorista
        - ((producto.precio_mayorista * producto.descuento_mayorista) / 100)
    )
    valor = "{0:.1f}".format(valor)
    return float(valor)


# *************************************************************************
# * TOMAR PRECIO FINAL
# *************************************************************************
@register.filter(name="precio_final_mayorista")
def precio_final_mayorista(productos, carro):
    # print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
    # print(productos)
    sum = 0
    for p in productos:
        sum += precio_total_producto_mayorista(p, carro)
    # print("BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB")

    sum = "{0:.1f}".format(sum)
    return sum


@register.filter(name="precio_final")
def precio_final(productos, carro):
    # print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
    # print(productos)
    sum = 0
    for p in productos:
        sum += precio_total_producto(p, carro)
    # print("BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB")
    sum = "{0:.1f}".format(sum)
    return float(sum)  # Devuelve como flotante


# *************************************************************************
# * ------------------
# *************************************************************************
@register.filter(name="producto_seleccionado")
def producto_seleccionado(producto, carro):
    # print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
    keys = carro.keys()
    for id in keys:
        if int(id) == producto.id:
            # print(producto.id)
            return '<span class="icon-carrito" style="background-color:green; "></span>'


@register.filter(name="retornar_imagen")
def retornar_imagen(producto):
    # print("ttttttttttttttttttttttt")
    # print(producto)
    el_articulo = Producto.objects.get(Q(articulo=producto))
    # print(el_articulo.imagen)
    return el_articulo.imagen
