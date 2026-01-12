
from django.http import HttpResponseRedirect
from usuario.models import Perfil
from usuario.forms import PerfilForm
from usuario.models import Perfil
from django.views.generic import CreateView
from django.urls import reverse
from django.utils.functional import cached_property
from django.views.generic import CreateView
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin

class EditPerfilPaso1(LoginRequiredMixin,CreateView):
    model = Perfil
    form_class = PerfilForm

    @cached_property
    def usuario(self,):
        # *********************************************************
        # 1) Primero obtengo el id del usuario
        # *********************************************************
        usuario = self.request.user
        return usuario

    @cached_property
    def perfil(self,):
        # *********************************************************
        # 1) Primero obtengo el id del usuario
        # *********************************************************
        perfil = Perfil.objects.get(usuario = self.request.user)
        return perfil

    def get_form_kwargs(self, **kwargs):
        form_kwargs = super().get_form_kwargs()
        form_kwargs["usuario"] = self.usuario
        return form_kwargs

    def get_success_url(self):
        return reverse('checkout')

    def form_valid(self, form):
        usuario = self.request.user
        instance, _ = Perfil.objects.get_or_create(usuario=usuario)
        instance.nombre = form.cleaned_data["nombre"]
        instance.apellido = form.cleaned_data["apellido"]
        instance.clave = form.cleaned_data["clave"]
        instance.provincia = form.cleaned_data["provincia"]
        instance.localidad = form.cleaned_data["localidad"]
        instance.domicilio = form.cleaned_data["domicilio"]
        instance.codigo_postal = form.cleaned_data["codigo_postal"]
        instance.telefono_fijo = form.cleaned_data["telefono_fijo"]
        instance.celular = form.cleaned_data["celular"]
        instance.cuil_cuit = form.cleaned_data["cuil_cuit"]
        instance.documento = form.cleaned_data["documento"] 
        instance.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["proceso"] = 1
        context["nombre"] = self.perfil.nombre
        context["apellido"] = self.perfil.apellido
        context["cuil_cuit"] = self.perfil.cuil_cuit
        context["domicilio"] = self.perfil.domicilio        
        context["localidad"] = self.perfil.localidad
        context["provincia"] = self.perfil.provincia
        context["documento"] = self.perfil.documento
        context["codigo_postal"] = self.perfil.codigo_postal
        context["celular"] = self.perfil.celular
        context["condicion_afip"] = self.perfil.condicion_afip
        context["razon_social"] = self.perfil.razon_social
        context["domicilio_comercial"] = self.perfil.domicilio_comercial
        return context