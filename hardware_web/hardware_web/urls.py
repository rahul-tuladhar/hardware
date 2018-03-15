from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
# from .views import

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^v3/users', include('login.urls')),
    url(r'^v3/posts', include('posts.urls')),
    # url(r'^v3/reviews/', include('reviews.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
