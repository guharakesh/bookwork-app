from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from student.models import Student
from student.forms import StudentForm, UserForm 
from django import forms
from django.forms import ModelForm

# Create your views here.
def splash(request):
    # return HttpResponse("Hey you're on the splaspage")
    if request.user.is_authenticated():
        new_student = Student.objects.get_or_create(user=request.user)[0]
        new_student.save()

        if request.method == "POST":

            userform = UserForm(request.POST or None, instance=request.user)

            if userform.is_valid():
                userlink = userform.save(commit=False)
                userlink.save()

            studentform = StudentForm(request.POST or None, instance=new_student)

            if studentform.is_valid():
                link = studentform.save(commit=False)
                link.save()

            #skillform = SkillForm(request.POST)

            #if skillform.is_valid():
                #skill_link = skillform.save(commit=False)
                #skill_link.save()
        else:
            userform = UserForm()
            studentform= StudentForm()
            #skillform = SkillForm()
        return render(request, 'splashpage/base_loggedin.html',{"studentform": studentform,"userform":userform})
    else:
        return render(request, 'splashpage/base_splashpage.html',{})

def login(request):
    # return HttpResponse("Hey you're on the splaspage")
    return render(request, 'splashpage/base_login.html',{})

def registration(request):
    # return HttpResponse("Hey you're on the splaspage")
    return render(request, 'splashpage/base_registration.html',{})
