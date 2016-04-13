# coding=utf-8
from __future__ import unicode_literals
# from django.http import HttpResponse
# from django.template import loader
from django.shortcuts import render
from django.views.generic import TemplateView
# from django.contrib.auth import login, logout
from imager.settings import MEDIA_URL
from imager_images.models import Photo
# from django.contrib.auth.views import login
import os


def home_page(request, * args, **kwargs):
    """View function for our home page."""
    foo = 'garbanzo beans'
    return render(request, 'home.html', context={'foo': foo})


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
