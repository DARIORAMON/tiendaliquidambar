from django.views.generic import View
from django.shortcuts import render
from django.db.models import Q
from django.contrib.sites.models import Site
from pedidos.models import Pedido

class FormaDePagoView(View):
    template = "pagos/forma_de_pago.html"

    def get(self, request):
        params = {}
        id_pedido = self.request.session["pedido_id"]
        pedido_id = Pedido.objects.get(Q(id=id_pedido)) 
        pedido_id.total
        params["pedido_id_total"]=pedido_id.total

        return render(request, self.template, params)