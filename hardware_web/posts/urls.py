from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import *

urlpatterns = [
    url(r'^home/$', home, name='home'),
    url(r'^post_detail/(?P<id>[0-9]+)$', post_detail, name='post_detail'),
    url(r'^add_post/$', add_post, name='add_post'),
    url(r'^register/$', register, name='register'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^search/$', search, name='search'),
] + staticfiles_urlpatterns()
