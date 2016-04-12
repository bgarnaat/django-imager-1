from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from imager_profile import ImagerProfile


PUBLISHED_OPTS = [
    ('private', 'Private'),
    ('shared', 'Shared'),
    ('public', 'Public'),
]


@python_2_unicode_compatible
class Photo(models.Model):
    """Photo model for imager photos."""
    image = models.ImageField(upload_to='photos/')
    owner = models.ForeignKey(ImagerProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    date_uploaded = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_noe=True)
    date_published = models.DateTimeField(auto_now=True)
    published = models.CharField(choices=PUBLISHED_OPTS)


@python_2_unicode_compatible
class Album(models.Model):
    """Album model for imager albums."""
    owner = models.ForeignKey(ImagerProfile, on_delete=models.CASCADE)
    photos = models.ManyToManyField(Photo, through='ImagerProfile')
    title = models.CharField(max_length=255)
    description = models.TextField()
    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_noe=True)
    date_published = models.DateTimeField(auto_now=True)
    published = models.CharField(choices=PUBLISHED_OPTS)
