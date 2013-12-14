from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from student.models import Student

# Create your views here.
def splash(request):
    # return HttpResponse("Hey you're on the splaspage")
    if request.user.is_authenticated():
        new_student = Student.objects.get_or_create(user=request.user)[0]
        new_student.save()
#       User.objects.filter(email=request.user.email)
#       if not Student.objects.filter(email=request.user.email):
#           new_student = Student(user=request.user)
#           new_student.save()
        return render(request, 'splashpage/base_loggedin.html',{})
    else:
        return render(request, 'splashpage/base_splashpage.html',{})

def login(request):
    # return HttpResponse("Hey you're on the splaspage")
    return render(request, 'splashpage/base_login.html',{})

def registration(request):
    # return HttpResponse("Hey you're on the splaspage")
    return render(request, 'splashpage/base_registration.html',{})
