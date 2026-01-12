from django.forms import ModelForm
from usuario.models import Perfil
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PerfilForm(ModelForm):
    class Meta:
        model = Perfil
        fields = [
            "nombre",
            "apellido",
            "clave",
            "provincia",
            "localidad",
            "domicilio",
            "codigo_postal",
            "telefono_fijo",
            "celular",
            "cuil_cuit",
            "documento",
            "condicion_afip",  
            "razon_social", 
            "domicilio_comercial", 
        ]
 

    def __init__(self, *args, **kwargs):
        # ****************************************************
        # Valor de pedido recibido desde view_crear.pedido()
        # ****************************************************
        self.usuario = kwargs.pop("usuario")
        super().__init__(*args, **kwargs)

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
