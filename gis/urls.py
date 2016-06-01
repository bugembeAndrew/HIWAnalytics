# urls for testapp module

from django.conf.urls import url, patterns
from . import views

urlpatterns = patterns("gis.views",
    url(r'^$', views.index, name='index'),
    url(r'^map/$', views.gis, name='map'),
    url(r'^density/$', views.density, name='density'),
)