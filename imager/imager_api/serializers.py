from rest_framework import serializers
from imager_images.models import Photo, Album


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
