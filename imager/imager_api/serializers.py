from rest_framework import serializers
from django.contrib.auth.models import User
from imager_images.models import Photo



class PhotoSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(
        view_name='photo-highlight', format='html')

    class Meta:
        model = Photo
        fields = ('image', 'owner', 'title', 'description', 'date_uploaded',
                  'date_modified', 'date_published', 'published',)
