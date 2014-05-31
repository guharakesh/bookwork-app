from django.contrib.sites.models import RequestSite
from django.contrib.sites.models import Site

class UserCookieMiddleware(object):
    def process_response(self, request, response):

        if Site._meta.installed:
            site = Site.objects.get_current()
        else:
            site = RequestSite(request)

        domain_name = '.' + site.domain

        if 'localhost' in domain_name:
            domain_name = ''
        else:
            domain_name = '.bookwork.co'

        if not hasattr(request, 'user'):
            if request.COOKIES.get('authed'):
                response.delete_cookie('authed')
            return response
        if request.user.is_authenticated() and not request.COOKIES.get('authed'):
            response.set_cookie('authed', value='True', domain=domain_name)
        elif not request.user.is_authenticated() and request.COOKIES.get('authed'):
            response.delete_cookie('authed')
        return response
