from django.conf.urls import patterns, include, url
from social_auth.middleware import SocialAuthExceptionMiddleware
from social_auth import exceptions as social_exceptions
from splashpage import views
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

urlpatterns = patterns('',
    url(r'^$', views.next, name='next'),
)

class SocialAuthExceptionMiddleware(SocialAuthExceptionMiddleware):
    def process_exception(self, request, exception):
         if hasattr(social_exceptions, 'AuthCanceled'):
            messages.add_message(request, messages.ERROR, 'SOCIAL CANCELED')
            return HttpResponseRedirect("/accounts/register") 
         else:
            raise exception