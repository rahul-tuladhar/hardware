from django.conf.urls import url
from .views import homepage, post_detail

urlpatterns = [
    url(r'^home/$', home, name='home'),
    url(r'^post_detail/(?P<p_id>[0-9]+)$', post_detail, name='post_detail')
]
