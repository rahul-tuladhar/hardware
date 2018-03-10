from django.conf.urls import url
from django.contrib import admin
from .views import user_profile

urlpatterns = [
    url(r'^(?P<username>\w{1,24})/$', user_profile)
]
