from rest_framework import serializers
from imager_images.models import Photo, Album


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        # fields = ('image', 'owner', 'title', 'description', 'date_uploaded',
        #           'date_modified', 'date_published', 'published',)


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        # fields = ('image', 'owner', 'title', 'description', 'date_uploaded',
        #           'date_modified', 'date_published', 'published',)
