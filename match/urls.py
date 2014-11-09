__author__ = 'arya'
from django.conf.urls import patterns, url

from match import views

urlpatterns = patterns('',
    url(r'^register$', views.register, name='register'),
    url(r'^createnew$', views.create_new, name='create_new'),
    url(r'^index$', views.index, name='index'),
    url(r'^$', views.index, name='index'),
    url(r'^success$', views.success, name='success'),
    url(r'^login$', views.login_view, name='login'),
    url(r'^logout$', views.logout_view, name='logout'),
    url(r'^profile$', views.profile, name='profile'),
    url(r'^profile/(\d+)/$', views.friend_profile, name='friend_profile'),
    url(r'^profile/(\d+)/send', views.send, name='send_message'),

    url(r'^interests$', views.add_interests, name='interests'),
    url(r'^find$', views.find_flight, name='find_flight'),
    url(r'^addflight$',views.addFlight, name='add_flight'),
    url(r'^flight/(\d+)/$', views.flight_page, name='flight_page'),
    url(r'^flight/(\d+)/seat$', views.choose_seat, name='choose_seat'),
    url(r'^flight/(\d+)/profiles$', views.flight_profiles, name='flight_profiles'),
    #url(r'^flight/(\d+)/hotel$', views.select_hotel, name='select_hotel'),

    url(r'^flight/(\d+)/hotel_select$', views.select_hotel, name='select_hotel'),


)
