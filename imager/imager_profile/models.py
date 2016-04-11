from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from django.utils.encoding import python_2_unicode_compatible


PHOTOGRAPHY_TYPES = [
    ('portrait', 'Portrait'),
    ('landscape', 'Landscape'),
    ('sports', 'Sports'),
    ('bw', 'Black and White'),
    ('nature', 'Nature'),
]
REGIONS = [
    ('pnw', 'Pacific Northwest'),
    ('ne', 'New England'),
    ('mdw', 'Midwest'),
    ('se', 'Southeast'),
    ('ma', 'Mid-Atlantic'),
    ('sw', 'Southwest'),
    ('mtw', 'Mountain West'),
    ('ca', 'California'),
    ('ak', 'Alaska'),
    ('hi', 'Hawaii'),
]


@python_2_unicode_compatible
class ImagerProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        related_name='profile'
    )
    camera_type = models.CharField(max_length=255)
    type_of_photography = models.CharField(
        max_length=128,
        choices=PHOTOGRAPHY_TYPES,
    )
    friends = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='friend_of'
    )
    region = models.CharField(
        max_length=3,
        choices=REGIONS,
    )
