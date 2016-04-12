from __future__ import unicode_literals
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django.conf import settings
from imager_profile.models import ImagerProfile


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile(sender, instance, **kwargs):
    profile = ImagerProfile(user=instance)
    profile.save()


@receiver(pre_delete, sender=settings.AUTH_USER_MODEL)
def delete_profile(sender, instance, **kwargs):
    instance.profile.delete()
