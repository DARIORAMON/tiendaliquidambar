from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView
from .forms import CrearPedidoForm
from .models import Item, Pedido
from productos.models.producto import Producto
from django.db.models import Q
from django.utils.functional import cached_property
from django.shortcuts import redirect
from usuario.models import Perfil
from decimal import Decimal

class Checkout(CreateView):
    model = Pedido
    form_class = CrearPedidoForm

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
        form_kwargs["email"] = self.usuario.email
        form_kwargs["nombre"] = self.perfil.nombre
        form_kwargs["apellido"] = self.perfil.apellido
        form_kwargs["cuil_cuit"] = self.perfil.cuil_cuit
        form_kwargs["domicilio"] = self.perfil.domicilio        
        form_kwargs["localidad"] = self.perfil.localidad
        form_kwargs["provincia"] = self.perfil.provincia
        form_kwargs["documento"] = self.perfil.documento
        form_kwargs["codigo_postal"] = self.perfil.codigo_postal
        form_kwargs["telefono"] = self.perfil.celular
        form_kwargs["condicion_afip"] = self.perfil.condicion_afip
        form_kwargs["razon_social"] = self.perfil.razon_social
        form_kwargs["domicilio_comercial"] = self.perfil.domicilio_comercial     
        return form_kwargs

    def form_valid(self, form):
        
        total = 0
        nombre_apellido_recibe= form.cleaned_data["nombre_apellido_recibe"]
        documento_recibe= form.cleaned_data["documento_recibe"]
        domicilio_recibe= form.cleaned_data["domicilio_recibe"]
        provincia_recibe= form.cleaned_data["provincia_recibe"]
        localidad_recibe= form.cleaned_data["localidad_recibe"]
        codigo_postal_recibe= form.cleaned_data["codigo_postal_recibe"]
        telefono_recibe= form.cleaned_data["telefono_recibe"]
        envio_otro =form.cleaned_data["envio_otro"]
        mi_pedido = Pedido(
            usuario  = self.request.user,
            nombre = self.perfil.nombre,
            email = self.usuario.email,
            apellido = self.perfil.apellido,
            cuil_cuit = self.perfil.cuil_cuit,
            domicilio = self.perfil.domicilio,
            localidad = self.perfil.localidad,
            provincia = self.perfil.provincia,
            codigo_postal = self.perfil.codigo_postal,
            documento = self.perfil.documento,
            telefono = self.perfil.celular,
            condicion_afip = self.perfil.condicion_afip,
            razon_social = self.perfil.razon_social,
            domicilio_comercial = self.perfil.domicilio_comercial,
            nombre_apellido_recibe = nombre_apellido_recibe, 
            documento_recibe =  documento_recibe,
            domicilio_recibe =  domicilio_recibe,
            localidad_recibe =  localidad_recibe,
            provincia_recibe =  provincia_recibe, 
            codigo_postal_recibe = codigo_postal_recibe ,
            telefono_recibe =  telefono_recibe,
            envio_otro = envio_otro,
        ) 
        # #######################################################
        # AQUÍ GUARDO EL PEDIDO
        # #######################################################
        mi_pedido.save()
        # #######################################################
        # VOY A AGREGAR AL PEDIDO LOS ITEMS
        # #######################################################
        ids = list(self.request.session.get("carro").keys())
        ids2 = []
        for id in ids:
            #print(id[:8])
            if id[:8] == "prestige":
                val = id[9:]
                val = int(val)
                ids2.append(val)     
        art_venta = Producto.objects.filter(pk__in=ids2)

        # #######################################################
        # CARGO LOS ITEMS AL PEDIDO
        # #######################################################
        for el_id in ids2:
            el_articulo = Producto.objects.get(id=el_id)
            cantidad = 0
            prod = "prestige_" + str(el_id)
            for x, y in self.request.session.get("carro").items():
                if x == prod:
                    cantidad = y
            Item.objects.create(
                pedido=mi_pedido,
                cada_producto=el_articulo,
                cantidad=cantidad,
                precio=el_articulo.precio,
                peso=el_articulo.peso,
                descuento=el_articulo.descuento,
            )
            el_precio = Decimal(cantidad) * (Decimal(el_articulo.precio) - ((Decimal(el_articulo.precio) * Decimal(el_articulo.descuento)) / 100))
            el_precio = "{0:.2f}".format(el_precio)
            total = Decimal(total) + Decimal(el_precio)
            total = "{0:.2f}".format(total)
        # #######################################################
        # CARGO EL TOTAL
        # #######################################################
        mi_pedido.total = total
        mi_pedido.save()
        # #######################################################
        # BORRAR VARIABLES DE SESIÓN DE PRODUCTOS Y 
        # CREAR VARIABLE DE SESIÓN DE PEDIDO
        # #######################################################
        self.request.session["pedido_id"] = mi_pedido.id
        return redirect(reverse("forma_de_pago"))

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        """ ***************************************************
        * DESDE AQUÍ PUEDO ENVIAR INFORMACIÓN A LA VISTA
        * POR LO QUE PASO LOS ARTICULOS 
        ****************************************************""" 
        productos = Producto.objects.filter(Q(estado="Publicado"))
        ids = list(self.request.session.get("carro").keys())
        ids2 = []
        for id in ids:
            print(id[:8])
            if id[:8] == "prestige":
                val = id[9:]
                val = int(val)
                ids2.append(val)     
        art_venta = Producto.objects.filter(pk__in=ids2)
        context["los_productos"] = art_venta
        return context
