from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your views here.
def splash(request):
    # return HttpResponse("Hey you're on the splaspage")
    if request.user.is_authenticated():
        if not User.objects.filter(email=request.user.email):
            new_student = Student(user=request.user)
        return render(request, 'splashpage/base_loggedin.html',{})
    else:
        return render(request, 'splashpage/base_splashpage.html',{})

def login(request):
    # return HttpResponse("Hey you're on the splaspage")
    return render(request, 'splashpage/base_login.html',{})

def registration(request):
    # return HttpResponse("Hey you're on the splaspage")
    return render(request, 'splashpage/base_registration.html',{})
