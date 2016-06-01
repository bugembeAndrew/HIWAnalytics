# urls for testapp module

from django.conf.urls import url, patterns
from django.views.generic import ListView
from art.views import ArtListView, ArtCreate, ArtUpdate, ArtDelete
from . import views

urlpatterns = patterns("art.views",
    url(r'^art/$', views.index, name='index'),
    url(r'^patients/$', ArtListView.as_view(), name='patients'),
    url(r'add/$', ArtCreate.as_view(), name='add'),
    url(r'update/(?P<pk>[0-9]+)/$', ArtUpdate.as_view(), name='update'),
    url(r'(?P<pk>[0-9]+)/delete/$', ArtDelete.as_view(), name='delete'),
)