# urls for testapp module

from django.conf.urls import url, patterns
from . import views

urlpatterns = patterns("art.views",
    url(r'^index/$', views.index, name='index'),
    url(r'^linechart/', views.create_linechart, name='linechart'),
    url(r'^piechart/', views.piechart, name='pie'),
    url(r'^piechart2/', views.piechartTest, name='pie2'),
    url(r'^piechartBaby/', views.piechartBaby, name='pie3'),
)