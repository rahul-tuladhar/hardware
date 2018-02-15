from django.conf.urls import url
from django.contrib import admin
from .views import posts_view

urlpatterns = [
    url(r'^posts/', posts_view)
]
