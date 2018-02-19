from django.conf.urls import url
from django.contrib import admin
from .views import post_detail, index

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^(?P<post_title>\w{1,24})/$', post_detail, name='post_detail')
]
