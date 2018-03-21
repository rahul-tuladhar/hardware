from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^home/$', home, name='home'),
    url(r'^post_detail/(?P<id>[0-9]+)$', post_detail, name='post_detail'),
    url(r'^edit_post/(?P<id>[0-9]+)$', edit_post, name='edit_post'),
    url(r'^add_post/$', add_post, name='add_post'),
]
