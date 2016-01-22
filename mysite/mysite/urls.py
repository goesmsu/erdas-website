from django.conf import settings
from django.conf.urls import include, url


urlpatterns = [
    url(r'^download/$', 'landsat.views.data_compile'),
]
