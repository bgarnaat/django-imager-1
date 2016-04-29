from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from imager_api import views

urlpatterns = [
    url(r'^photo_list/$', views.PhotoList.as_view()),
    url(r'^photo_detail/(?P<pk>[0-9]+)/$', views.PhotoDetail.as_view()),
    url(r'^album_list/$', views.AlbumList.as_view()),
    url(r'^album_detail/(?P<pk>[0-9]+)/$', views.AlbumDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
