from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login
from .models import *
from django.contrib import messages
from usuario.decoradores import usuario_no_registrado


@usuario_no_registrado
def pagina_login(request):
    params = {}
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("tienda")
        else:
            messages.info(request, "El usuario o el password es incorrecto")
            return render(request, "usuario/login.html", params)
    return render(request, "usuario/login.html", params)