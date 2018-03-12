from django.contrib import admin
from django.conf.urls import url, include
from posts.views import index

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^user/', include('login.urls')),
    url(r'^posts/', include('posts.urls')),
]
