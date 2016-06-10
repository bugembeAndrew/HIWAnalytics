from django.conf.urls import patterns, include, url 
from . import views
urlpatterns = patterns('myapp.views',      
	#url(r'^$', views.home, name='home'),
    url(r'^linechart/', views.create_linechart, name='linechart'),
    url(r'^piechart/', views.piechart, name='pie'),
    url(r'^piechart2/', views.piechartTest, name='pie2'),
    url(r'^piechartBaby/', views.piechartBaby, name='pie3'),
    url(r'^help/', views.helpPage, name='help'),
) 