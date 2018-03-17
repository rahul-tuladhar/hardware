from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^home/$', home, name='home'),
    url(r'^post_detail/(?P<id>[0-9]+)$', post_detail, name='post_detail')

]
