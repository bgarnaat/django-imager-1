# coding=utf-8
from __future__ import unicode_literals
from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.contrib.auth import logout
from imager.settings import STATIC_URL
from imager_images.models import Photo, Album
from imager_profile.models import ImagerProfile
from django.contrib.auth.models import User
from django.forms import ModelForm
from datetime import datetime as flegal

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
            img_url = os.path.join(STATIC_URL, 'imager', 'neil.jpg')
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
        album_cover = []
        for item in album:
            try:
                album_cover.append((item.photos.all()[0].image.url, item.id))
            except IndexError:
                album_cover.append((
                    os.path.join(STATIC_URL, 'imager', 'neil.jpg'), item.id))
        return {
            'album_cover': album_cover,
            'album_qty': album_qty,
            'img': img,
            'img_qty': img_qty,
            }


class AlbumView(TemplateView):
    template_name = 'album.html'

    def get_context_data(self, *args, **kwargs):
        try:
            album = Album.objects.get(pk=kwargs['id'])
            photos = album.photos.all()
            img_qty = photos.count()
        except IndexError:
            album = None
            photos = []
        return {'album': album, 'img_qty': img_qty, 'photos': photos}


class PhotoView(TemplateView):
    template_name = 'photo.html'

    def get_context_data(self, *args, **kwargs):
        try:
            img = Photo.objects.get(pk=kwargs['id'])
        except IndexError:
            img = None
        return {'img': img}


class AlbumForm(ModelForm):
    class Meta:
        model = Album
        fields = ['photos', 'title', 'description', 'published']


class AddAlbumView(TemplateView):
    template_name = 'add_album.html'

    def get_context_data(self, *args, **kwargs):
        form = AlbumForm()
        form.fields['photos'].queryset = Photo.objects.all().filter(
            owner=self.request.user)
        return {'form': form}

    def post(self, request, *args, **kwargs):
        form = AlbumForm(self.request.POST)
        if self.request.method == 'POST' and form.is_valid():
            form.instance.owner = request.user
            form.instance.date_published = flegal.now().isoformat()
            form.save()
        return redirect('library')


class PhotoForm(ModelForm):
    class Meta:
        model = Photo
        fields = ['image', 'title', 'description', 'published']


class AddPhotoView(TemplateView):
    template_name = 'add_photo.html'

    def get_context_data(self, *args, **kwargs):
        form = PhotoForm()
        return {'form': form}

    def post(self, request, *args, **kwargs):
        form = PhotoForm(request.POST, request.FILES)
        if request.method == 'POST' and form.is_valid():
            form.instance.owner = request.user
            form.instance.date_published = flegal.now().isoformat()
            form.save()
        return redirect('library')


class EditAlbumView(TemplateView):
    template_name = 'add_album.html'

    def get_context_data(self, *args, **kwargs):
        album_edit = Album.objects.get(pk=kwargs['id'])
        data = {
            'photos': album_edit.photos.all(),
            'title': album_edit.title,
            'description': album_edit.description,
            'published': album_edit.published,
        }
        form = AlbumForm(initial=data)
        form.fields['photos'].queryset = Photo.objects.all().filter(
            owner=self.request.user)
        return {'form': form}

    def post(self, request, *args, **kwargs):
        form = AlbumForm(
            self.request.POST, instance=Album.objects.get(pk=kwargs['id']))
        if self.request.method == 'POST' and form.is_valid():
            form.instance.owner = request.user
            form.save()
        return redirect('library')


class PhotoEditForm(ModelForm):
    class Meta:
        model = Photo
        fields = ['title', 'description', 'published']


class EditPhotoView(TemplateView):
    template_name = 'add_photo.html'

    def get_context_data(self, *args, **kwargs):
        img = Photo.objects.get(pk=kwargs['id'])
        data = {
            'title': img.title,
            'description': img.description,
            'published': img.published
        }
        form = PhotoEditForm(initial=data)
        return {'form': form, 'img': img.image.url}

    def post(self, request, *args, **kwargs):
        form = PhotoForm(
            request.POST, request.FILES, instance=Photo.objects.get(
                pk=kwargs['id']))
        if request.method == 'POST' and form.is_valid():
            form.instance.owner = request.user
            form.save()
        return redirect('library')


class DeleteAlbumView(TemplateView):

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            Album.objects.get(pk=kwargs['id']).delete()
        return redirect('library')


class DeletePhotoView(TemplateView):

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            Photo.objects.get(pk=kwargs['id']).delete()
        return redirect('library')


class ProfileEditForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']


class ImagerProfileEditForm(ModelForm):
    class Meta:
        model = ImagerProfile
        fields = ['camera_type', 'type_of_photography', 'friends', 'region']


class ProfileEditView(TemplateView):
    template_name = 'edit_profile.html'

    def get_context_data(self, *args, **kwargs):
        data1 = {
            'username': self.request.user.username,
            'email': self.request.user.email,
        }
        form1 = ProfileEditForm(initial=data1)

        profile = ImagerProfile.objects.get(user=self.request.user)
        data2 = {
            'camera_type': profile.camera_type,
            'type_of_photography': profile.type_of_photography,
            'friends': profile.friends.all(),
            'region': profile.region,
        }

        form2 = ImagerProfileEditForm(initial=data2)
        return {'form1': form1, 'form2': form2}

    def post(self, request, *args, **kwargs):
        form1 = ProfileEditForm(request.POST, instance=User.objects.get(
            username=request.user.username))
        form2 = ImagerProfileEditForm(
            request.POST, instance=ImagerProfile.objects.get(
                user=request.user))
        if request.method == 'POST' and form1.is_valid() and form2.is_valid():
            form2.instance.user = request.user
            form1.save()
            form2.save()
        return redirect('library')
