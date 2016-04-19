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
from .views import ClassView, logout_view, ProfileView, LibraryView, AlbumView, PhotoView
from django.conf.urls.static import static
from imager import settings


# TODO: WRAP URLS IN LOGIN REQUIRED...  it will solve every problem ever, for realy-yo...
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', ClassView.as_view(), name='home_page'),
    # url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', logout_view),
    url(r'^accounts/', include('registration.backends.hmac.urls')),
    url(r'^accounts/profile/$', ProfileView.as_view(), name='profile'),
    url(r'^images/library/$', LibraryView.as_view(), name='library'),
    url(r'^images/album/(?P<id>[0-9])$', AlbumView.as_view(), name='album'),
    url(r'^images/photo/(?P<id>[0-9])$', PhotoView.as_view(), name='photo'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
