__author__ = 'arya'
from django.conf.urls import patterns, url

from match import views

urlpatterns = patterns('',
    url(r'register', views.register, name='register'),
    url(r'createnew', views.create_new, name='create_new')
)
