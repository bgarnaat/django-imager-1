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
        response = self.client.get('/images/album/1')
        self.assertEquals(response.status_code, 200)

    def test_PhotoView(self):
        """Test photo view for a specific user."""
        self.client.force_login(self.user)
        response = self.client.get('/images/photo/3')
        self.assertEquals(response.status_code, 200)
