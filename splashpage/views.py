from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from student.models import Student
from student.forms import StudentForm
from django import forms
from django.forms import ModelForm

# Create your views here.
def splash(request):
    # return HttpResponse("Hey you're on the splaspage")
    if request.user.is_authenticated():
        new_student = Student.objects.get_or_create(user=request.user)[0]
        new_student.save()
        if request.method == "POST":
            formset = StudentForm(request.POST or None, instance=new_student)
            if formset.is_valid():
                link = formset.save(commit=False)

                link.save()
        else:
            formset = StudentForm()
        return render(request, 'splashpage/base_loggedin.html',{"formset": formset})
    else:
        return render(request, 'splashpage/base_splashpage.html',{})

def login(request):
    # return HttpResponse("Hey you're on the splaspage")
    return render(request, 'splashpage/base_login.html',{})

def registration(request):
    # return HttpResponse("Hey you're on the splaspage")
    return render(request, 'splashpage/base_registration.html',{})
