from django.conf.urls import url, include
from imager_api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'imager_api', views.PhotoViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
