from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from .models import *
from .forms import CreateUserForm
from usuario.decoradores import usuario_no_registrado


@usuario_no_registrado
def pagina_registro(request):

    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get("username")
            messages.success(
                request, "La cuenta se ha creado exitosamente para: " + user
            )

            return redirect("login")
    params = {}
    params["form"] = form
    return render(request, "usuario/registro.html", params)