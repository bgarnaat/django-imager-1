from django.test import TestCase, Client
from imager_profile.models import ImagerProfile
from django.contrib.auth.models import User
import factory


class UserFactory(factory.django.DjangoModelFactory):
    """Set up User Factory."""
    class Meta:
        model = User

    username = factory.Faker('user_name')
    email = factory.Faker('email')
    password = factory.Faker('password')


class UserProfileTest(TestCase):
    """Test user profiles."""

    def setUp(self):
        """Initialize a test user."""
        self.user = UserFactory.create()

    def test_user_profile(self):
        """Test if user has a profile."""
        self.assertIsInstance(self.user.profile, ImagerProfile)

    def test_user_profile_active(self):
        """Test user profile active."""
        self.assertTrue(self.user.profile.is_active)

    def test_user_profile_camera(self):
        """Test user profile camera field."""
        self.user.camera_type = 'Holga'
        self.assertEqual(self.user.camera_type, 'Holga')

    def test_user_profile_region(self):
        """Test user profile region."""
        self.user.region = 'mtw'
        self.assertEqual(self.user.region, 'mtw')

    def test_user_profile_type_of_photography(self):
        """Test user profile type of photography."""
        self.user.type_of_photography = 'bw'
        self.assertEqual(self.user.type_of_photography, 'bw')

    def test_user_delete(self):
        """Test for deleting users."""
        self.user.delete()
        self.assertFalse(self.user.profile in ImagerProfile.active.all())

    def test_user_already_created_check(self):
        """Test post save handler."""
        self.user.camera_type = 'Canon'
        self.user.save()
        self.assertEqual(self.user.camera_type, 'Canon')


class ViewTests(TestCase):
    def setUp(self):
        """Set up test client."""
        self.client = Client()
        self.user = UserFactory.create()

    def test_homepage(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_register(self):
        response = self.client.get('/accounts/register', follow=True)
        self.assertEquals(response.status_code, 200)

    def test_login(self):
        response = self.client.post(
            '/accounts/login', {'username': self.user.username,
                                'password': self.user.password}, follow=True)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(
            response.redirect_chain[0], ('/accounts/login/', 301))

    def test_logout(self):
        response = self.client.get('/logout', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEquals(
            response.redirect_chain[0], ('/logout/', 301))
    #
    # def test_activate(self):
    #     response = self.client.get('/accounts/activate')
    #     self.assertEqual(response.status_code, 200)
