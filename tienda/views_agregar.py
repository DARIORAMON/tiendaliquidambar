import json
from django.http import HttpResponse
from productos.models.producto import Producto


def agregar(request, *args, **kwargs):
    if request.method == "GET":
        idproducto = request.GET.get("cada_producto_id")
        valor = request.GET.get("valor")
        carro = request.session.get("carro")
        # ###########################################
        # RECUPERO PRODUCTO PARA LIMITAR STOCK
        # ###########################################
        idproducto_rec = idproducto[9:]
        idproducto_rec = int(idproducto_rec)
        el_prod = Producto.objects.get(id=idproducto_rec)
        print(el_prod.stock)
        print("stock")
        stock_actual = int(el_prod.stock)
        if int(valor) >= stock_actual:
            cantida = int(valor)
        else:
            cantida = int(valor) + 1
        # ###########################################
        # ACTUALIZO VARIABLE DE SESSION
        # ###########################################
        carro[idproducto] = cantida
        request.session["carro"] = carro
        # ###########################################
        # FIN
        # ###########################################
        print("bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb")
        results = []
        data = {}
        data["idproducto"] = str(idproducto)
        data["cantida"] = str(cantida)
        results.append(data)
        data_json = json.dumps(results)
        mimetype = "application/json"
        return HttpResponse(data_json, mimetype)