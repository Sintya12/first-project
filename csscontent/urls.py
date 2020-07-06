from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^(?P<slug>[\w-]+)/$', ContentDetail.as_view(), name='content'),
    url(r'^mengenal/cascadingstylesheet/$', ContentList.as_view(), name='definisi'),
    url(r'^$', Page.as_view(), name='page'),
]
