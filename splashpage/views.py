from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from student.models import Student
from django.forms.models import modelformset_factory

# Create your views here.
def splash(request):
    # return HttpResponse("Hey you're on the splaspage")
    StudentFormSet = modelformset_factory(Student)
    if request.user.is_authenticated():
        new_student = Student.objects.get_or_create(user=request.user)[0]
        new_student.save()
        if request.method == "POST":
            formset = StudentFormSet(request.POST, request.FILES, queryset=Student.objects.filter(user=request.user))
            if formset.is_valid():
                formset.save()
        else:
            formset = StudentFormSet(queryset=Student.objects.filter(user=request.user))
        return render(request, 'splashpage/base_loggedin.html',{"formset": formset})
    else:
        return render(request, 'splashpage/base_splashpage.html',{})

def login(request):
    # return HttpResponse("Hey you're on the splaspage")
    return render(request, 'splashpage/base_login.html',{})

def registration(request):
    # return HttpResponse("Hey you're on the splaspage")
    return render(request, 'splashpage/base_registration.html',{})
