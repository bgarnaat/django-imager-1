from django.test import TestCase, Client
from imager_images.tests import PhotoFactory, AlbumFactory
from imager_profile.tests import UserFactory
import json


class ViewTests(TestCase):
    """Test API views."""

    def setUp(self):
        """Set up test client."""
        self.client = Client()
        self.user = UserFactory.create()
        self.photo = PhotoFactory.create(
            owner=self.user,
        )
        self.album = AlbumFactory.create(
            owner=self.user,
        )

    def test_photo_list_view(self):
        """Test photo list api view."""
        response = self.client.get('/photo_list/')
        json_dict = json.loads(response.content.decode())
        self.assertEquals(response.status_code, 200)
        self.assertEqual(json_dict['results'], [])

    def test_photo_logged_in_list_view(self):
        """Test photo list api view while logged in."""
        self.client.force_login(self.user)
        response = self.client.get('/photo_list/')
        json_dict = json.loads(response.content.decode())
        self.assertEquals(response.status_code, 200)
        self.assertEquals(json_dict['results'][0]['id'], self.photo.id)

    def test_photo_detail_view(self):
        """Test photo list api view."""
        self.client.force_login(self.user)
        photo_id = self.photo.id
        response = self.client.get('/photo_detail/{}/'.format(photo_id))
        json_dict = json.loads(response.content.decode())
        self.assertEquals(response.status_code, 200)
        self.assertEquals(json_dict['id'], photo_id)

    def test_album_list_view(self):
        """Test album list api view."""
        response = self.client.get('/album_list/')
        json_dict = json.loads(response.content.decode())
        self.assertEquals(response.status_code, 200)
        self.assertEqual(json_dict['results'], [])

    def test_album_logged_in_list_view(self):
        """Test photo list api view while logged in."""
        self.client.force_login(self.user)
        response = self.client.get('/album_list/')
        json_dict = json.loads(response.content.decode())
        self.assertEquals(response.status_code, 200)
        self.assertEquals(json_dict['results'][0]['id'], self.album.id)

    def test_album_detail_view(self):
        """Test album list api view."""
        self.client.force_login(self.user)
        album_id = self.album.id
        response = self.client.get('/album_detail/{}/'.format(album_id))
        json_dict = json.loads(response.content.decode())
        self.assertEquals(response.status_code, 200)
        self.assertEquals(json_dict['id'], album_id)
