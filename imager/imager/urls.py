"""imager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from .views import ClassView, logout_view, ProfileView, LibraryView
from .views import AlbumView, AddAlbumView, EditAlbumView, DeleteAlbumView
from .views import PhotoView, AddPhotoView, EditPhotoView, DeletePhotoView
from django.conf.urls.static import static
from imager import settings
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', ClassView.as_view(), name='home_page'),
    # url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', logout_view),
    url(r'^accounts/', include('registration.backends.hmac.urls')),
    url(r'^accounts/profile/$',
        login_required(ProfileView.as_view()),
        name='profile'),
    url(r'^images/library/$',
        login_required(LibraryView.as_view()),
        name='library'),
    url(r'^images/album/(?P<id>[0-9]+)$',
        login_required(AlbumView.as_view()),
        name='album'),
    url(r'^images/albums/add/$',
        login_required(AddAlbumView.as_view()),
        name='add_album'),
    url(r'^images/albums/edit/(?P<id>[0-9]+)$',
        login_required(EditAlbumView.as_view()),
        name='edit_album'),
    url(r'^images/albums/delete/(?P<id>[0-9]+)$',
        login_required(DeleteAlbumView.as_view()),
        name='delete_album'),
    url(r'^images/photo/(?P<id>[0-9]+)$',
        login_required(PhotoView.as_view()),
        name='photo'),
    url(r'^images/photos/add/$',
        login_required(AddPhotoView.as_view()),
        name='add_photo'),
    url(r'^images/photos/edit/(?P<id>[0-9]+)$',
        login_required(EditPhotoView.as_view()),
        name='edit_photo'),
    url(r'^images/photos/delete/(?P<id>[0-9]+)$',
        login_required(DeletePhotoView.as_view()),
        name='delete_photo'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
