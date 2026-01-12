from django.urls import path
from pedidos.views_checkout import Checkout
from pedidos.views_politica import PaginaPolitica
from pedidos.views_perfil_paso1 import EditPerfilPaso1

urlpatterns = [
    path("checkout/", Checkout.as_view(), name="checkout"),
    path("politica/", PaginaPolitica.as_view(), name="politica"),
    path("perfil_paso1/", EditPerfilPaso1.as_view(), name="perfil_paso1"),
]