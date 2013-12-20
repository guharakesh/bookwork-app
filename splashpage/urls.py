import autocomplete_light
autocomplete_light.autodiscover()

from django.conf.urls import patterns, include, url

from splashpage import views

urlpatterns = patterns('',
    url(r'^$', views.splash, name='splash'),
    url(r'^login/', views.login, name='login'),
    url(r'^registration/', views.registration, name='registration')
)
