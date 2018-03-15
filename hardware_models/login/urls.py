from .views import user_profile, index
from django.conf.urls import url

urlpatterns = [
    url(r'^/profile/$', index, name='index'),
    url(r'^/(?P<username>\w{1,24})/$', user_profile, name= 'user_profile')
]
