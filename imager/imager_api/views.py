from imager_images.models import Photo
from imager_api.serializers import PhotoSerializer
from rest_framework.response import Response
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.decorators import detail_route


class PhotoViewSet(viewsets.ModelViewSet):
    """Set photo view."""
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        photo = self.get_object()
        return Response(photo.highlighted)
