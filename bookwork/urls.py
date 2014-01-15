from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout
from django.contrib import admin
from registration.backends.default.views import RegistrationView
from registration.backends.default.views import ActivationView
from registration.forms import RegistrationFormUniqueEmail
from django.contrib.auth.decorators import user_passes_test
import splashpage

admin.autodiscover()

login_forbidden = user_passes_test(lambda u: u.is_anonymous(), '/')

class RegistrationFormUniqueEmailNoUsername(RegistrationFormUniqueEmail):

    cleaned_data['username'] = cleaned_data['email']

    def __init__(self, *args, **kwargs):
        super (RegistrationFormUniqueEmailNoUsername, self).__init__(*args, **kwargs)
        self.fields.pop('username')

class RegistrationViewUniqueEmailNoUsername(RegistrationView):
    form_class = RegistrationFormUniqueEmailNoUsername

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bookwork.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^$', 'splashpage.views.splash', name='splash'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^splash/', include('splashpage.urls', namespace="splashpage")),
    # url(r'^$', 'splashpage.views.splash', name='home')
    # url(r'^homepage/', include('homepage.urls',namespace="homepage"))
    url(r'^accounts/register$', login_forbidden(RegistrationViewUniqueEmailNoUsername.as_view()), name='registration_register'),
    url(r'^accounts/login$', login_forbidden(login), name='login'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    # (r'^login/?$','django.contrib.auth.views.login',{'template_name':'registraion/login.html', 'authentication_form':MyAuthenticationForm}),
)
