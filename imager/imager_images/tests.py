from django.test import TestCase, override_settings
# from django.db.models import ImageField
# from django.db.models.fields.files import ImageFieldFile
from imager_images.models import Photo, Album
from imager_profile.tests import UserFactory
import factory


# @override_settings(MEDIA_ROOT='/tmp')
class PhotoFactory(factory.django.DjangoModelFactory):
    """Set up Photo Factory."""
    class Meta:
        model = Photo
    image = factory.django.ImageField(filename='/tmp/image01.jpg')
    date_published = '2016-04-11'


class AlbumFactory(factory.django.DjangoModelFactory):
    """Set up Photo Factory."""
    class Meta:
        model = Album
    date_published = '2016-04-11'


# @override_settings(MEDIA_ROOT='/tmp/')
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

    def test_photo_has_id(self):
        """Test photo has an id."""
        self.assertTrue(self.photo.id)

    def test_photo_instance(self):
        """Assert self is instance of Photo."""
        self.assertIsInstance(self.photo, Photo)

    def test_photo_description(self):
        """Test photo title field."""
        self.photo.description = 'A summer day.'
        self.assertEqual(self.photo.description, 'A summer day.')

    def test_published_default(self):
        """Test if public is published default."""
        self.assertEqual(self.photo.published, 'public')


class AlbumTest(TestCase):
    """Test album models."""

    def setUp(self):
        """Initialize an album."""
        self.user = UserFactory.create()
        self.album = AlbumFactory.create(
            owner=self.user,
        )

    def test_album_title(self):
        """Test album title field."""
        self.album.title = 'Outside'
        self.assertEqual(self.album.title, 'Outside')

    def test_album_published_default(self):
        """Test if public is published default."""
        self.assertEqual(self.album.published, 'public')

    def test_album_instance(self):
        """Assert self is instance of Photo."""
        self.assertIsInstance(self.album, Album)

    def test_album_description(self):
        """Test album title field."""
        self.album.description = 'A summer day.'
        self.assertEqual(self.album.description, 'A summer day.')
