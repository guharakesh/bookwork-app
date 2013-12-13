from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def splash(request):
    # return HttpResponse("Hey you're on the splaspage")
    if request.user.is_authenticated():
        return HttpResponse("Hey you're on the splashpage")
    else:
        return render(request, 'splashpage/base_splashpage.html',{})

def login(request):
    # return HttpResponse("Hey you're on the splaspage")
    return render(request, 'splashpage/base_login.html',{})

def registration(request):
    # return HttpResponse("Hey you're on the splaspage")
    return render(request, 'splashpage/base_registration.html',{})
