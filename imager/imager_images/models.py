from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from django.utils.encoding import python_2_unicode_compatible
from imager_profile.models import ImagerProfile


PUBLISHED_OPTS = [
    ('private', 'Private'),
    ('shared', 'Shared'),
    ('public', 'Public'),
]


@python_2_unicode_compatible
class Photo(models.Model):
    """Photo model for imager photos."""
    image = models.ImageField(upload_to='photos/')
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    date_uploaded = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)
    date_published = models.DateTimeField()
    published = models.CharField(
        max_length=20,
        choices=PUBLISHED_OPTS,
        default='public'
    )


@python_2_unicode_compatible
class Album(models.Model):
    """Album model for imager albums."""
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    photos = models.ManyToManyField(Photo)
    title = models.CharField(max_length=255)
    description = models.TextField()
    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)
    date_published = models.DateTimeField()
    published = models.CharField(
        max_length=20,
        choices=PUBLISHED_OPTS,
        default='public'
    )
