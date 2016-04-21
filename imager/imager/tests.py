from django.test import TestCase, Client
from imager_images.tests import PhotoFactory, AlbumFactory
from imager_profile.tests import UserFactory


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

    # def test_LibraryView_no_login(self):
    #     """Test library view for a specific user."""
    #     # self.client.force_login(self.user)
    #     # import pdb; pdb.set_trace()
    #     response = self.client.get('/images/library/', follow=True)
    #     self.assertEquals(response.status_code, 200)
    #     self.assertEquals(
    #         response.redirect_chain[0], ('/images/library/', 301))

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
