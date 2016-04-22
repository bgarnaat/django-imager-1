from django.test import TestCase, Client
from imager_images.tests import PhotoFactory, AlbumFactory
from imager_profile.tests import UserFactory
from imager_images.models import Photo, Album


class ViewTests(TestCase):
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

    def test_homepage(self):
        """Test homepage view."""
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_register(self):
        """Test register view."""
        response = self.client.get('/accounts/register', follow=True)
        self.assertEquals(response.status_code, 200)

    def test_login(self):
        """Test for login view."""
        response = self.client.post(
            '/accounts/login', {'username': self.user.username,
                                'password': self.user.password}, follow=True)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(
            response.redirect_chain[0], ('/accounts/login/', 301))

    def test_logout(self):
        """Test for logout view."""
        response = self.client.get('/logout', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEquals(
            response.redirect_chain[0], ('/logout/', 301))

    def test_activate(self):
        """Test activate with no activation key."""
        response = self.client.get('/accounts/activate', follow=True)
        self.assertEqual(response.status_code, 404)

    def test_LibraryView(self):
        """Test library view for a specific user."""
        self.client.force_login(self.user)
        response = self.client.get('/images/library/')
        self.assertEquals(response.status_code, 200)

    def test_AlbumView(self):
        """Test album view for a specific user."""
        self.client.force_login(self.user)
        response = self.client.get('/images/album/{}'.format(self.album.id))
        self.assertEquals(response.status_code, 200)

    def test_PhotoView(self):
        """Test photo view for a specific user."""
        self.client.force_login(self.user)
        response = self.client.get('/images/photo/{}'.format(self.photo.id))
        self.assertEquals(response.status_code, 200)

    def test_AlbumEditView(self):
        """Test album edit view."""
        self.client.force_login(self.user)
        response = self.client.get(
            '/images/albums/edit/{}'.format(self.album.id))
        self.assertEquals(response.status_code, 200)

    def test_AlbumEditView_post(self):
        """Test album edit view."""
        self.client.force_login(self.user)
        temp_title = self.album.title
        self.album.title = 'new title'
        self.client.post('/images/albums/edit/{}'.format(self.album.id))
        self.assertNotEqual(self.album.title, temp_title)
        self.assertEquals(self.album.title, 'new title')

    def test_PhotoEditView(self):
        """Test album edit view."""
        self.client.force_login(self.user)
        response = self.client.get(
            '/images/photos/edit/{}'.format(self.photo.id))
        self.assertEquals(response.status_code, 200)

    def test_PhotoEditView_post(self):
        """Test album edit view."""
        self.client.force_login(self.user)
        temp_title = self.photo.title
        self.photo.title = 'new title'
        self.client.post('/images/photos/edit/{}'.format(self.photo.id))
        self.assertNotEqual(self.photo.title, temp_title)
        self.assertEquals(self.photo.title, 'new title')

    def test_PhotoEditView_nologin(self):
        response = self.client.get(
            '/images/photos/edit/{}'.format(self.photo.id))
        self.assertIn('/accounts/login', response.url)
        self.assertEquals(response.status_code, 302)

    def test_AlbumEditView_nologin(self):
        response = self.client.get(
            '/images/albums/edit/{}'.format(self.album.id))
        self.assertIn('/accounts/login', response.url)
        self.assertEquals(response.status_code, 302)

    def test_PhotoAddView(self):
        """Test photo add view."""
        self.client.force_login(self.user)
        response = self.client.get('/images/photos/add/')
        self.assertEquals(response.status_code, 200)

    def test_PhotoAddView_nologin(self):
        """Test photo add view no login."""
        response = self.client.get('/images/photos/add/')
        self.assertIn('/accounts/login', response.url)
        self.assertEquals(response.status_code, 302)

    def test_AlbumAddView(self):
        """Test album add view."""
        self.client.force_login(self.user)
        response = self.client.get('/images/albums/add/')
        self.assertEquals(response.status_code, 200)

    def test_AlbumAddView_nologin(self):
        """Test album add view no login."""
        response = self.client.get('/images/albums/add/')
        self.assertIn('/accounts/login', response.url)
        self.assertEquals(response.status_code, 302)

    def test_ProfileEditView(self):
        """Test profile edit view."""
        self.client.force_login(self.user)
        response = self.client.get('/profile/edit/')
        self.assertEquals(response.status_code, 200)

    def test_ProfileEditView_post(self):
        """Test profile edit view."""
        self.client.force_login(self.user)
        temp_title = self.user.username
        self.user.username = 'new username'
        self.client.post('/profile/edit/')
        self.assertNotEqual(self.user.username, temp_title)
        self.assertEquals(self.user.username, 'new username')

    def test_ProfileEditView_nologin(self):
        """Test profile edit view no login."""
        response = self.client.get('/profile/edit/')
        self.assertIn('/accounts/login', response.url)
        self.assertEquals(response.status_code, 302)

    def test_PhotoDeleteView(self):
        """Test photo delete view."""
        self.client.force_login(self.user)
        response = self.client.post(
            '/images/photos/delete/{}'.format(self.photo.id))
        with self.assertRaises(Photo.DoesNotExist):
            Photo.objects.get(id=self.photo.id)
        self.assertEquals(response.status_code, 302)

    def test_AlbumDeleteView(self):
        """Test photo delete view."""
        self.client.force_login(self.user)
        response = self.client.post(
            '/images/albums/delete/{}'.format(self.album.id))
        with self.assertRaises(Album.DoesNotExist):
            Album.objects.get(id=self.album.id)
        self.assertEquals(response.status_code, 302)
