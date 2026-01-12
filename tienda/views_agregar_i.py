import json
from django.http import HttpResponse


def agregar_i(request, *args, **kwargs):
    if request.method == "GET":
        idproducto = request.GET.get("cada_producto_id")
        valor = request.GET.get("valor")
        carro = request.session.get("carro")
        cantida = int(valor)
        # ###########################################
        # CREO VARIABLE DE SESSION
        # ###########################################
        if carro:
            carro[idproducto] = cantida
        else:
            carro = {}
            carro[idproducto] = cantida
        request.session["carro"] = carro
        # ###########################################
        # FIN
        # ###########################################
        results = []
        data = {}
        data["idproducto"] = str(idproducto)
        data["cantida"] = str(cantida)
        results.append(data)
        data_json = json.dumps(results)
        mimetype = "application/json"
        return HttpResponse(data_json, mimetype)