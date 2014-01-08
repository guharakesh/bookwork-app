from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from student.models import Student, Skill
from student.forms import StudentForm, UserForm, SkillForm
from django import forms
from django.forms import ModelForm

# Create your views here.
def splash(request):
    # return HttpResponse("Hey you're on the splaspage")
    if request.user.is_authenticated():
        new_student = Student.objects.get_or_create(user=request.user)[0]
        new_student.save()

        if request.method == "POST":

            skillform= SkillForm(request.POST or None)

            if 'new_skill' in request.body:
                if skillform.is_valid():
                    skill_text = skillform.cleaned_data['skill_text']
                    new_skill = Skill.objects.create(skill_text=skill_text)
                    new_skill.save()

                userform = UserForm(request.POST or None)
                studentform = StudentForm(request.POST or None)

            else:

                userform = UserForm(request.POST or None, instance=request.user)
    
                if userform.is_valid():
                    userlink = userform.save(commit=False)
                    userlink.save()
    
                studentform = StudentForm(request.POST or None, instance=new_student)
    
                if studentform.is_valid():
                    link = studentform.save(commit=False)
                    link.save()
    
                studentform.save_m2m()

        else:
            userform = UserForm(request.POST or None)
            studentform = StudentForm(request.POST or None)
            skillform = SkillForm(request.POST or None)
        return render(request, 'splashpage/base_loggedin.html',{"studentform": studentform,"userform":userform,"skillform":skillform})
    else:
        return render(request, 'splashpage/base_splashpage.html',{})

def login(request):
    # return HttpResponse("Hey you're on the splaspage")
    return render(request, 'splashpage/base_login.html',{})

def registration(request):
    # return HttpResponse("Hey you're on the splaspage")
    return render(request, 'splashpage/base_registration.html',{})
