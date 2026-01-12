import json
from django.http import HttpResponse


def quitar(request, *args, **kwargs):
    if request.method == "GET":
        print("1111111aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        idproducto = request.GET.get("cada_producto_id")
        valor = request.GET.get("valor")
        carro = request.session.get("carro")
        cantida = int(valor) - 1
        # ###########################################
        # ACTUALIZO VARIABLE DE SESSION
        # ###########################################
        carro[idproducto] = cantida
        request.session["carro"] = carro
        # ###########################################
        # FIN
        # ###########################################

        print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        print(idproducto)
        print(valor)
        print(cantida)
        print(carro)
        results = []
        data = {}
        data["idproducto"] = str(idproducto)
        data["cantida"] = str(cantida)
        results.append(data)
        data_json = json.dumps(results)
        mimetype = "application/json"
        return HttpResponse(data_json, mimetype)