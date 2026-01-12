from django.urls import path
from presentacion.views import Index
from presentacion.views import PreguntasFrecuentesVista

urlpatterns = [
    path("", Index.as_view(), name="home"),
    path("preguntas_frecuentes", PreguntasFrecuentesVista.as_view(), name="preguntas_frecuentes"),
]
