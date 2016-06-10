# urls for testapp module

from django.conf.urls import url, patterns
from . import views

urlpatterns = patterns("bayes.views",
    url(r'^calls/$', views.calls, name='calls'),
    url(r'^analytics/$', views.bayes, name='analytics'),
)