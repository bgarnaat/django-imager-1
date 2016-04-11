from django.db import models
from django.conf import settings


PHOTOGRAPHY_TYPES = [
    ('portrait', 'Portrait'),
    ('landscape', 'Landscape'),
    ('sports', 'Sports'),
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


class ImagerProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        related_name='profile'
    )
