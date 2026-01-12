from django.urls import path
from usuario.views_perfil import EditPerfil
from usuario import views_login
from usuario import views_logout
from usuario import views_registro
from usuario import views_perfil


urlpatterns = [
    path("login/", views_login.pagina_login, name="login"),
    path("logout/", views_logout.pagina_logout, name="logout"),
    path("registro/", views_registro.pagina_registro, name="registro"),
    path("perfil/", EditPerfil.as_view(), name="perfil"),
]