from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import render
from contacto.models import Consulta
from contacto.forms import ConsultaForm
from django.views.generic.edit import FormView
from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import render
from contacto.models import Consulta
from contacto.forms import ConsultaForm
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.conf import settings


class Contacto(View):

    template = 'contacto/contacto.html'

    def get(self, request):
        form = ConsultaForm()
        params = {}
        params['form'] = form
        usuario = request.user
        try:
            params["usuario"] = request.user
        except:
            print("---------  No estás logueado ")
        return render(request, self.template, params)

    def post(self, request):
        form = ConsultaForm(request.POST or None)
        if form.is_valid():
            for key in form.cleaned_data:
                print(key)

            nombre = form.cleaned_data["nombre"]
            descripcion = form.cleaned_data["descripcion"]
            mail = form.cleaned_data["mail"]
            #estado_respuesta = form.cleaned_data["estado_respuesta"]
            telefono = form.cleaned_data["telefono"]
            #fecha = form.cleaned_data["fecha"]

            print(nombre)
            print(descripcion)
            print(mail)
            #print(estado_respuesta)
            print(telefono)
            #print(fecha)

            send_mail(
                form.cleaned_data["nombre"],  
                form.cleaned_data["descripcion"],             
                settings.EMAIL_HOST_USER,
                ['liquidambar.almacen.natural@gmail.com'],
                fail_silently=False,
            )

            #com = Consulta(nombre=nombre, descripcion=descripcion, mail=mail, estado_respuesta='No Contestada', telefono=telefono, fecha=fecha)
            com = Consulta(nombre=nombre, descripcion=descripcion, mail=mail, telefono=telefono)
            com.save()

        else:
            print("aaaaaaaaaaaaaaaaaaaaaaaaaa")
        return HttpResponseRedirect('/contacto/mensaje_enviado')

class MensajeEnviado(View):

    template = 'contacto/mensaje_enviado.html'

    def get(self, request):
        form = ConsultaForm()
        params = {}
        params['form'] = form
        return render(request, self.template, params)