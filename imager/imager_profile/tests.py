from django.test import TestCase
from imager_profile.models import ImagerProfile
from django.contrib.auth.models import User
import factory


class UserFactory(factory.django.DjangoModelFactory):
    """Set up User Factory."""
    class Meta:
        model = User

    username = 'Joe'


class UserProfileTest(TestCase):
    """Test user profiles."""

    def setUp(self):
        """Initialize a test user."""
        self.user = UserFactory.create()
        self.user.save()

    def test_user_profile(self):
        """Test if user has a profile."""
        self.assertIsInstance(self.user.profile, ImagerProfile)
    #
    # def test_user_profile_active(self):
    #     """Test user profile active."""
    #     self.assertTrue(self.user.profile.is_active)
