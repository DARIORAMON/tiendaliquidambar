#from crispy_forms.helper import FormHelper
#from crispy_forms.layout import Div, Field, Fieldset, Layout, Submit
from django import forms
from .models import Pedido
from django.core.validators import RegexValidator

class CrearPedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = [
            "envio_otro",
            "nombre_apellido_recibe",
            "documento_recibe",
            "domicilio_recibe",
            "localidad_recibe",
            "provincia_recibe",
            "codigo_postal_recibe",
            "telefono_recibe",
        ]

    def __init__(self, *args, **kwargs):
        # ****************************************************
        # Valor de pedido recibido desde view_crear.pedido()
        # ****************************************************
        self.usuario = kwargs.pop("usuario")
        self.email = kwargs.pop("email")
        self.nombre = kwargs.pop("nombre")
        self.apellido = kwargs.pop("apellido")
        self.cuil_cuit = kwargs.pop("cuil_cuit")
        self.domicilio = kwargs.pop("domicilio")
        self.localidad = kwargs.pop("localidad")
        self.provincia = kwargs.pop("provincia")
        self.codigo_postal = kwargs.pop("codigo_postal")
        self.telefono = kwargs.pop("telefono")
        self.documento = kwargs.pop("documento")
        self.condicion_afip = kwargs.pop("condicion_afip")
        self.razon_social = kwargs.pop("razon_social")
        self.domicilio_comercial = kwargs.pop("domicilio_comercial")
        #self.tipo = kwargs.pop("tipo")
        super().__init__(*args, **kwargs)
