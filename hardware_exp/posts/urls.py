from django.conf.urls import url
from .views import homepage, post_detail

urlpatterns = [
    url(r'^home/', homepage, name='home'),
    url(r'^$', post_detail, name='post_detail')
]
