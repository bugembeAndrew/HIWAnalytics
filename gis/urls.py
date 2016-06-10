# urls for testapp module

from django.conf.urls import url, patterns
from . import views

urlpatterns = patterns("gis.views",
    url(r'^map/$', views.gis, name='map'),
    url(r'^patient/$', views.gis, name='patient'),
    url(r'^hospitals/$', views.density, name='hospitals'),
)