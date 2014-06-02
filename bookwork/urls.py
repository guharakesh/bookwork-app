from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout, password_change
from django.contrib import admin
from registration.backends.default.views import RegistrationView
from registration.backends.default.views import ActivationView
from registration.forms import RegistrationFormUniqueEmail
from django.contrib.auth.decorators import user_passes_test, login_required
from django import forms
from django.contrib.sites.models import Site
from django.contrib.sites.models import RequestSite
from registration.models import RegistrationProfile
from registration import signals
from django.contrib.auth.forms import AuthenticationForm
from splashpage.views import dash, user_settings, splash, current_employers
import string, random

admin.autodiscover()

login_forbidden = user_passes_test(lambda u: u.is_anonymous(), '/')


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

class AuthenticationFormWithEmail(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super (AuthenticationFormWithEmail, self).__init__(*args, **kwargs)

        self.fields['username'].label = 'Email'

class RegistrationFormUniqueEmailNoUsername(RegistrationFormUniqueEmail):
    

    def __init__(self, *args, **kwargs):
  

        super (RegistrationFormUniqueEmailNoUsername, self).__init__(*args, **kwargs)
        #self.fields.pop('username')
        self.fields['username'].widget = forms.HiddenInput()
        self.fields['username'].initial = id_generator()
        self.fields.insert(0,'last_name',forms.CharField())
        self.fields.insert(0,'first_name',forms.CharField())
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True

class RegistrationViewUniqueEmailNoUsername(RegistrationView):
    form_class = RegistrationFormUniqueEmailNoUsername
    allow_anon = True

    def register(self, request, **cleaned_data):
        username, email, password, first_name, last_name = cleaned_data['email'], cleaned_data['email'], cleaned_data['password1'], cleaned_data['first_name'], cleaned_data['last_name']
        if Site._meta.installed:
            site = Site.objects.get_current()
        else:   
            site = RequestSite(request)
        new_user = RegistrationProfile.objects.create_inactive_user(username, email,
                                                                    password, site)
        signals.user_registered.send(sender=self.__class__,
                                     user=new_user,
                                     request=request)
        
        new_user.first_name = first_name
        new_user.last_name = last_name
        new_user.save()

        return new_user

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bookwork.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^polls/', include('polls.urls', namespace="polls")),
    # url(r'^$', 'splashpage.views.splash', name='splash'),
    url(r'^$', login_required(dash), name='dash'),
    url(r'^next/', include('splashpage.urls', namespace='splash')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'', include('social_auth.urls')),

    url(r'^accounts/login$', login_forbidden(login),{'template_name':'registration/login.html','authentication_form':AuthenticationFormWithEmail}, name='login'),
    url(r'^accounts/register$', login_forbidden(RegistrationViewUniqueEmailNoUsername.as_view()), name='registration_register'),

    url(r'^settings/$', login_required(user_settings)),
    url(r'^settings/password/change/$', 'django.contrib.auth.views.password_change', {'template_name': 'registration/password_change_form.html'}, name='password_change'),
    url(r'^settings/password/change/done/$', 'django.contrib.auth.views.password_change_done', {'template_name': 'registration/password_change_done.html'}, name='password_change_done'),

    url(r'^accounts/password/reset/$', 'django.contrib.auth.views.password_reset', {'template_name': 'registration/password_reset_form.html'}, name='password_reset'),
    url(r'^accounts/password/reset/done/$', 'django.contrib.auth.views.password_reset_done', {'template_name': 'registration/password_reset_done.html'}, name='password_reset_done'),
    url(r'^accounts/password/reset/(?P<uidb36>[0-9A-Za-z]{1,13})-(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm_uidb36', {'template_name': 'registration/password_reset_confirm.html'}),
    url(r'^acccounts/password/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm', {'template_name': 'registration/password_reset_confirm.html'},
        name='password_reset_confirm'),
    url(r'^accounts/password/reset/complete/$', 'django.contrib.auth.views.password_reset_complete', {'template_name': 'registration/password_reset_complete.html'}, name='password_reset_complete'),

    url(r'^accounts/', include('registration.backends.default.urls')),

    url(r'^dash/', login_required(dash), name='dash'),
    url(r'^edit/', login_required(splash),name='splash'),
    url(r'^current_employers/',login_required(current_employers),name='current_employers'),
)
