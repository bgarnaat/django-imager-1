# coding=utf-8
from __future__ import unicode_literals
from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.contrib.auth import logout
from imager.settings import MEDIA_URL
from imager_images.models import Photo, Album
from django.contrib.auth.models import User
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


class ProfileView(TemplateView):
    template_name = 'profile.html'

    def get_context_data(self):
        img_qty = Photo.objects.all().filter(owner=self.request.user).count()
        album_qty = Album.objects.all().filter(owner=self.request.user).count()
        return {'album_qty': album_qty, 'img_qty': img_qty}


class LibraryView(TemplateView):
    template_name = 'library.html'

    def get_context_data(self):
        album = Album.objects.all().filter(owner=self.request.user)
        album_qty = album.count()
        img = Photo.objects.all().filter(owner=self.request.user)
        img_qty = img.count()
        try:
            album_cover = [(item.photos.all()[0].image.url, item.id) for item in album]
        except IndexError:
            album_cover = os.path.join(MEDIA_URL, 'neil.jpg')
        return {
            'album_cover': album_cover,
            'album_qty': album_qty,
            'img': img,
            'img_qty': img_qty,
            }


class AlbumView(TemplateView):
    template_name = 'album.html'

    def get_context_data(self, *arg, **kwargs):
        try:
            album = Album.objects.all().filter(id=kwargs['id'])[0]
            photos = album.photos.all()
            img_qty = photos.count()
        except IndexError:
            album = None
            photos = []
        return {'album': album, 'img_qty': img_qty, 'photos': photos}


class PhotoView(TemplateView):
    template_name = 'photo.html'

    def get_context_data(self, *arg, **kwargs):
        try:
            img = Photo.objects.all().filter(id=kwargs['id'])[0]
        except IndexError:
            img = None
        return {'img': img}
