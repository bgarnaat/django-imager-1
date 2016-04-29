from imager_images.models import Photo, Album
from imager_api.serializers import PhotoSerializer, AlbumSerializer
from rest_framework import generics


class PhotoList(generics.ListAPIView):
    serializer_class = PhotoSerializer

    def get_queryset(self):
        owner = self.request.user
        try:
            return Photo.objects.all().filter(owner=owner)
        except:
            return []


class PhotoDetail(generics.RetrieveAPIView):
    serializer_class = PhotoSerializer
    queryset = Photo.objects.all()

    def get_queryset(self):
        owner = self.request.user
        try:
            return Photo.objects.all().filter(owner=owner)
        except:
            return []

class AlbumList(generics.ListAPIView):
    serializer_class = AlbumSerializer

    def get_queryset(self):
        owner = self.request.user
        try:
            return Album.objects.all().filter(owner=owner)
        except:
            return []


class AlbumDetail(generics.RetrieveAPIView):
    serializer_class = AlbumSerializer
    queryset = Album.objects.all()

    def get_queryset(self):
        owner = self.request.user
        try:
            return Album.objects.all().filter(owner=owner)
        except:
            return []
