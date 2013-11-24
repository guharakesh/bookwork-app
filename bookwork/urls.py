from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout
from django.contrib import admin
import splashpage

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bookwork.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^splash/', include('splashpage.urls', namespace="splashpage")),
    # url(r'^$', 'splashpage.views.splash', name='home')
    # url(r'^homepage/', include('homepage.urls',namespace="homepage"))
    url(r'^accounts/', include('registration.backends.default.urls')),
    # (r'^login/?$','django.contrib.auth.views.login',{'template_name':'registraion/login.html', 'authentication_form':MyAuthenticationForm}),
)
