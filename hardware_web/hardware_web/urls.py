from django.conf.urls import url, include
from django.contrib import admin
# from .views import

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^v3/user/', include('login.urls')),
    url(r'^v3/posts/', include('posts.urls')),
    # url(r'^v3/reviews/', include('reviews.urls')),
]
