from django.apps import AppConfig


class ImagerProfileConfig(AppConfig):
    name = 'imager_profile'

    def ready(self):
        """To run when app is ready."""
        from imager_profile import handlers
