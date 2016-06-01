# urls for reports module

from django.conf.urls import url, patterns
from . import views

urlpatterns = patterns("reports.views",
    url(r'^$', views.index, name='index'),
    url(r'^arvs/$', views.arvs, name='arvs'),
    url(r'^age/$', views.age, name='age'),
    url(r'^challenges/$', views.challenges, name='challenges'),
)