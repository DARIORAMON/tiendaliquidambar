from django.shortcuts import render
from django.shortcuts import redirect
from productos.models.categoria import Categoria
from django.contrib.auth.models import User
import json
from django.http import HttpResponse
import ast

# from .models.cliente import Cliente
from productos.models.producto import Producto
from django.db.models import Q
from django.views.generic import View
from django.http import HttpResponseRedirect


def comprar(request, *args, **kwargs):
    if request.method == "GET":
        person = request.GET

        """ ######################################
        # CONVERTIR FORMATO DE JSON A DICCIONARIO
        # Y GUARDAR EN VARIABLE DE SESSION
        ##########################################"""
        print(person)

        print(type(person))
        print(person.dict())
        producto_formato_diccionario = person.dict()
        print(producto_formato_diccionario)
        print(producto_formato_diccionario["producto"])
        print(type(producto_formato_diccionario["producto"]))
        print("-----------------------------------------------")
        producto_dict = ast.literal_eval(producto_formato_diccionario["producto"])
        print(producto_dict)
        print(type(producto_dict))
        # request.session["carro"] = producto_formato_diccionario["producto"]
        # request.session["carro"] = producto_dict
        print("-----------------------------------------------")

        results = []
        data = {}
        # data["idproducto"] = str(idproducto)
        # data["cantida"] = str(cantida)
        # results.append(data)
        # print(results)
        data_json = json.dumps(results)

        mimetype = "application/json"
        return HttpResponse(data_json, mimetype)
