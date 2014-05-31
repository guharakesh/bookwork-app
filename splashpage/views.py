from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from student.models import Student, Skill
from employer.models import Employer
from student.forms import StudentForm, UserForm, SkillForm
from splashpage.forms import TypeForm
from django import forms
from django.forms import ModelForm
from django.contrib.auth.views import login
from django.contrib import messages
from django.db.models import Q
import pdb

# Create your views here.

def next(request):
    return render(request, 'splashpage/whats_next.html',{}) 

def splash(request):
    new_student = request.user.student
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

                messages.success(request, 'You\'re all set!')

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

def dash(request):
    new_student = request.user.student

    skills = []
    for skill in Skill.objects.filter(student=new_student):
        skills.append(skill)

    return render(request, 'splashpage/dash.html',{'skills':skills})

def current_employers(request):
    new_student = request.user.student

    employers = Employer.objects.all().order_by('name')
    return render(request, 'splashpage/current_employers.html',{'employers':employers})

