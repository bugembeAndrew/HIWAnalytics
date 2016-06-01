# urls for testapp module

from django.conf.urls import url, patterns
from . import views

urlpatterns = patterns("bayes.views",
    url(r'^$', views.index, name='index'),
    url(r'^analytics/$', views.bayes, name='analytics'),
)