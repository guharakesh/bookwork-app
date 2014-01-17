from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout
from django.contrib import admin
from registration.backends.default.views import RegistrationView
from registration.backends.default.views import ActivationView
from registration.forms import RegistrationFormUniqueEmail
from django.contrib.auth.decorators import user_passes_test
from django import forms
from django.contrib.sites.models import Site
from django.contrib.sites.models import RequestSite
from registration.models import RegistrationProfile
from registration import signals
from django.contrib.auth.forms import AuthenticationForm
import splashpage, string, random

admin.autodiscover()

login_forbidden = user_passes_test(lambda u: u.is_anonymous(), '/')

class AuthenticationFormWithEmail(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        self.fields['username'].label = 'Email'

class RegistrationFormUniqueEmailNoUsername(RegistrationFormUniqueEmail):
    def __init__(self, *args, **kwargs):
        super (RegistrationFormUniqueEmailNoUsername, self).__init__(*args, **kwargs)
        #self.fields.pop('username')
        self.fields['username'].widget = forms.HiddenInput()
        self.fields['username'].initial = id_generator()

class RegistrationViewUniqueEmailNoUsername(RegistrationView):
    form_class = RegistrationFormUniqueEmailNoUsername

    def register(self, request, **cleaned_data):
        """
        Given a username, email address and password, register a new
        user account, which will initially be inactive.

        Along with the new ``User`` object, a new
        ``registration.models.RegistrationProfile`` will be created,
        tied to that ``User``, containing the activation key which
        will be used for this account.

        An email will be sent to the supplied email address; this
        email should contain an activation link. The email will be
        rendered using two templates. See the documentation for
        ``RegistrationProfile.send_activation_email()`` for
        information about these templates and the contexts provided to
        them.

        After the ``User`` and ``RegistrationProfile`` are created and
        the activation email is sent, the signal
        ``registration.signals.user_registered`` will be sent, with
        the new ``User`` as the keyword argument ``user`` and the
        class of this backend as the sender.

        """
        username, email, password = cleaned_data['email'], cleaned_data['email'], cleaned_data['password1']
        if Site._meta.installed:
            site = Site.objects.get_current()
        else:
            site = RequestSite(request)
        new_user = RegistrationProfile.objects.create_inactive_user(username, email,
                                                                    password, site)
        signals.user_registered.send(sender=self.__class__,
                                     user=new_user,
                                     request=request)
        return new_user
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
