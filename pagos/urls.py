from django.urls import path
from pagos.views import FormaDePagoView

urlpatterns = [
    path("forma_de_pago", FormaDePagoView.as_view(), name="forma_de_pago"),
]
