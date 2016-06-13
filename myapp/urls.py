from django.conf.urls import patterns, include, url 
from . import views
urlpatterns = patterns('myapp.views',      
    url(r'^ages/', views.create_linechart, name='ages'),
    url(r'^ratios/', views.piechart, name='ratios'),
    url(r'^spouses/', views.piechartTest, name='spouses'),
    url(r'^babies/', views.piechartBaby, name='babies'),
    url(r'^help/', views.helpPage, name='help'),
) 