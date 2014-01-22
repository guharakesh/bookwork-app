from django.conf.urls import patterns, include, url

from splashpage import views

urlpatterns = patterns('',
    url(r'^$', views.splash, name='splash'),
)
