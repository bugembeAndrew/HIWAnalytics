"""mywebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include, patterns
from . import views
from .views import RecommendationsListView

urlpatterns = patterns('spouseBabyTestedFeatures.views',
    url(r'^recommendation/$', views.index, name = 'recommendation'),
    url(r'^baby_analytical_graphs/$', views.baby_analytical_graphs, name = 'baby_analytical_graphs'),
    url(r'^spouse_analytical_graphs/$', views.spouse_analytical_graphs, name = 'spouse_analytical_graphs'),
    url(r'^spouse_not_tested/$', views.spouse_not_tested, name = 'spouse_not_tested'),
    url(r'^baby_not_tested/$', views.baby_not_tested, name = 'baby_not_tested'),
    url(r'^view_sent_recommendations/$', RecommendationsListView.as_view(), name = 'view_sent_recommendations'),
    url(r'^baby_recommendation/$', views.SendSmsToPatientWhoseBabyNotTestedCreateView.as_view(), name = 'recommendation'),
    url(r'^spouse_recommendation/$', views.SendSmsToPatientWhoseSpouseNotTestedCreateView.as_view(), name = 'recommendation'),
    url(r'^baby_not_tested/baby_recommendation/$', views.SendSmsToPatientWhoseBabyNotTestedCreateView.as_view(), name = 'recommendation'),
    url(r'^spouse_not_tested/spouse_recommendation/$', views.SendSmsToPatientWhoseSpouseNotTestedCreateView.as_view(), name = 'recommendation'),
    url(r'^message_patients/$', views.message_patients, name = 'recommendation1'),
    url(r'^message_sent_successfully/$', views.message_sent_successfully, name = 'message_sent_successfully'),
 )
