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
# from .views import home_page
from .views import ClassView
from django.conf.urls.static import static
from imager import settings
# from django.contrib.auth.views import login

# image_urls = []
# profile_urls = []
# api_urls = []
#
# urlpatterns = image_urls + profile_urls + api_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', ClassView.as_view(), name='home_page'),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    # url(r'^registration/(?P<id>[0-9]+)$', ClassView.as_view(), name='home_page'),
    # url(r'^home/(?P<id>[0-9]+)$', home_page, name='home_page'),
    # url(r'^profile/', imager_profile.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
