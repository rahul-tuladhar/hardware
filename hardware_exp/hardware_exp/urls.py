from django.conf.urls import url, include
from django.contrib import admin
# from .views import

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^user/', include('login.urls')),
    url(r'^posts/', include('posts.urls')),
    url(r'^reviews/', include('reviews.urls')),
]
