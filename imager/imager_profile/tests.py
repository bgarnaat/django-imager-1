from django.test import TestCase
from imager_profile.models import ImagerProfile
from django.contrib.auth.models import User
import factory


class UserFactory(factory.django.DjangoModelFactory):
    """Set up User Factory."""
    class Meta:
        model = User

    username = 'Bob'


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

    def test_user_delete(self):
        """Test for deleting users."""
        self.user.delete()
        self.assertFalse(self.user.profile in ImagerProfile.active.all())
