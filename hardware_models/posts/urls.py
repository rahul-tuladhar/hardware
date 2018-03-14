from django.conf.urls import url
from .views import post_detail, index, edit_post

urlpatterns = [
    url(r'^/home$', index, name='index'),
    url(r'^/(?P<id>\d+)/$', post_detail, name='post_detail'),
    url(r'^/(?P<id>\d+)/edit/$', edit_post, name='edit_post'),
]
