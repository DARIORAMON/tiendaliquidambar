from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from usuario.models import Perfil


# #################################################################
# PARA PERFIL
# ################################################################


@receiver(post_save, sender=User)
def create_perfil(sender, instance, created, **kwargs):

    if created:
        Perfil.objects.create(usuario=instance)
        print("Se han creado los datos de usuario")


@receiver(post_save, sender=User)
def update_perfil(sender, instance, created, **kwargs):

    if created == False:
        instance.perfil.save()
        print("perfil actualizado")
