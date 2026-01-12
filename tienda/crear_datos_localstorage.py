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


def crear_localstorage(request, *args, **kwargs):
    if request.method == "GET":
        person = request.GET
        """ ######################################
        # CONVERTIR FORMATO DE JSON A DICCIONARIO
        # Y GUARDAR EN VARIABLE DE SESSION
        ##########################################"""
        producto_formato_diccionario = person.dict()
        producto_dict = ast.literal_eval(producto_formato_diccionario["producto"])
        request.session["carro"] = producto_dict
        results = []
        data = {}
        data_json = json.dumps(results)
        mimetype = "application/json"
        return HttpResponse(data_json, mimetype)
