from django.conf.urls import url
from .views import homepage
from .views import post_detail

urlpatterns = [
    url(r'^/home/', homepage, name='home'),
    url(r'^/(?P<id>\d+)/$', post_detail, name='post_detail')
]
