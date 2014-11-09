__author__ = 'arya'
from django.conf.urls import patterns, url

from match import views

urlpatterns = patterns('',
    url(r'register', views.register, name='register'),
    url(r'createnew', views.create_new, name='create_new'),
    url(r'index', views.index, name='index'),
    url(r'^$', views.index, name='index'),
    url(r'success', views.success, name='success'),
    url(r'login', views.login_view, name='login'),
    url(r'logout', views.logout_view, name='logout'),
    url(r'profile', views.profile, name='profile'),
    url(r'interests', views.add_interests, name='interests'),
)
