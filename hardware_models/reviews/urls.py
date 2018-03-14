from django.conf.urls import url
from .views import review_detail

urlpatterns = [
    url(r'^/(?P<review_id>\d+)/$', review_detail, name='review_detail'),
]
