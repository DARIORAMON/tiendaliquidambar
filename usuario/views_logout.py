from django.shortcuts import render
from django.contrib.auth import logout
from .models import *

def pagina_logout(request):
    template = "usuario/el_logout.html"
    params = {}
    logout(request)
    return render(request, template, params)