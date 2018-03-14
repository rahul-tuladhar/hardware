from django.conf.urls import url
from .views import post_detail, index, edit_post

urlpatterns = [
    url(r'^/home$', index, name='index'),
    url(r'^/(?P<post_title>\w{1,24})/$', post_detail, name='post_detail'),
    url(r'^/(?P<post_title>\w{1,24})/edit$', edit_post, name='edit_post'),
]
