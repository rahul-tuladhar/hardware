from django.conf.urls import url, include
from django.contrib import admin
# from .views import

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('posts.urls')),
]
