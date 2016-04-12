from django.test import TestCase
from django.db.models import ImageField
from django.db.models.fields.files import ImageFieldFile
from imager_images.models import Photo, Album
from imager_profile.models import ImagerProfile
from imager_profile.tests import UserFactory
import factory


class PhotoFactory(factory.django.DjangoModelFactory):
    """Set up Photo Factory."""
    class Meta:
        model = Photo
    image = factory.django.ImageField(filename='/tmp/image01.jpg')
    # date_created = '2016-04-11'


class PhotoTest(TestCase):
    """Test photo models."""

    def setUp(self):
        """Initialize a photo."""
        self.user = UserFactory.create()
        self.photo = PhotoFactory.create(
            owner=self.user,
        )

    def test_photo_title(self):
        """Test photo title field."""
        self.photo.title = 'Outside'
        self.assertEqual(self.photo.title, 'Outside')
