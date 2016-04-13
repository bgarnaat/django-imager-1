# coding=utf-8
from __future__ import unicode_literals
from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.contrib.auth import logout
from imager.settings import MEDIA_URL
from imager_images.models import Photo
import os


def logout_view(request):
    logout(request)
    return redirect('home_page')


class ClassView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self):
        try:
            img = Photo.objects.all().filter(
                published='public').order_by('?')[0]
            img_url = img.image.url
        except IndexError:
            img_url = os.path.join(MEDIA_URL, 'neil.jpg')
        return {'img_url': img_url}
