from django.conf.urls import url, include
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

from .views import *

urlpatterns = [
    url(r'^blog/', include('blog.urls', namespace = 'blog')),
    url(r'^django/', include('djangocontent.urls', namespace = 'django')),
    url(r'^oop/', include('oopcontent.urls', namespace = 'oop')),
    url(r'^python/', include('pythoncontent.urls', namespace = 'python')),
    url(r'^bootstrap/', include('bootstrapcontent.urls', namespace = 'bootstrap')),
    url(r'^dom/', include('domcontent.urls', namespace = 'dom' )),
    url(r'^js/', include('jscontent.urls', namespace = 'js' )),
    url(r'^css/', include('csscontent.urls', namespace = 'css' )),
    url(r'^html/', include('htmlcontent.urls', namespace = 'html' )),
    url(r'^tutorial/$', Tutorial.as_view(), name='tutorial'),
    url(r'^$', Home.as_view(), name='home'),
    url(r'^admin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
