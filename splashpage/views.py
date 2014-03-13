from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from student.models import Student, Skill
from student.forms import StudentForm, UserForm, SkillForm, EmailForm
from django import forms
from django.forms import ModelForm
from django.contrib.auth.views import login
from django.contrib import messages
from django.db.models import Q

# Create your views here.

def next(request):
    return render(request, 'splashpage/whats_next.html',{}) 

def splash(request):
    # return HttpResponse("Hey you're on the splashpage")
    if request.user.is_authenticated():
        request.user.username = request.user.email
        request.user.save()
        new_student = Student.objects.get_or_create(user=request.user)[0]
        new_student.save()

        if request.method == "POST":

            skillform = SkillForm(request.POST or None)

            if 'new_skill' in request.body:
                if skillform.is_valid():
                    skill_text = skillform.cleaned_data['skill_text']
                    new_skill = Skill.objects.get_or_create(skill_text__iexact=skill_text,defaults={'skill_text':skill_text,'creator':request.user})[0]
                    new_skill.save()

                    userform = UserForm(request.POST or None)
                    studentform = StudentForm(request.POST or None)
                    skill_ids = []
                    for skill in Skill.objects.filter(student=new_student):
                        skill_ids.append(skill.id)

                    for skill_id in request.POST.getlist('skills'):
                        skill_ids.append(skill_id)
 
                    skill_ids.append(new_skill.id)
        
                    studentform = StudentForm(
                        initial = {'year_in_school': new_student.year_in_school,
                                   'school': new_student.school,
                                   'skills': skill_ids
                                  },
                    )
                    studentform.fields['skills'].queryset = Skill.objects.filter(Q(approved=True) | Q(creator=request.user))

                    skillform = SkillForm()

            else:

                userform = UserForm(request.POST or None, instance=request.user)
    
                if userform.is_valid():
                    userlink = userform.save(commit=False)
                    userlink.save()
    
                studentform = StudentForm(request.POST or None, instance=new_student)
                studentform.fields['skills'].queryset = Skill.objects.filter(Q(approved=True) | Q(creator=request.user))
    
                if studentform.is_valid():
                    link = studentform.save(commit=False)
                    link.save()
    
                    studentform.save_m2m()

                    messages.success(request, 'You\'re all set! So what comes next?')

        else:
            userform = UserForm(
                request.POST or None,
                initial = {'first_name': request.user.first_name,
                           'last_name': request.user.last_name
                          }
            )

            skill_ids = []
            for skill in Skill.objects.filter(student=new_student):
                skill_ids.append(skill.id)

            studentform = StudentForm(
                request.POST or None, 
                initial = {'year_in_school': new_student.year_in_school,
                           'school': new_student.school,
                           'skills': skill_ids
                          }
            )
            studentform.fields['skills'].queryset = Skill.objects.filter(Q(approved=True) | Q(creator=request.user))
            skillform = SkillForm(
                request.POST or None
            )
        return render(request, 'splashpage/base_loggedin.html',{'studentform': studentform,'userform':userform,'skillform':skillform})
    elif request.user.is_authenticated() and not user.email:
        emailform = EmailForm()
        return render(request, 'splashpage/require_email.html',{'emailform':emailform})
    else:
        return render(request, 'splashpage/base_splashpage.html',{})

def dash(request):
    if request.user.is_authenticated():
        request.user.username = request.user.email
        request.user.save()
        new_student = Student.objects.get_or_create(user=request.user)[0]
        new_student.save()
        return render(request, 'splashpage/dash.html',{})
    else:
        return render(request, 'splashpage/base_splashpage.html',{})

def current_employers(request):
    if request.user.is_authenticated():
        request.user.username = request.user.email
        request.user.save()
        new_student = Student.objects.get_or_create(user=request.user)[0]
        new_student.save()
        return render(request, 'splashpage/current_employers.html',{})
    else:
        return render(request, 'splashpage/base_splashpage.html',{})