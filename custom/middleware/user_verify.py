from django.http import HttpResponse, HttpResponseRedirect
from student.models import Student
from employer.models import Employer
from splashpage.forms import TypeForm
from django.shortcuts import render, redirect
from django.middleware.csrf import rotate_token

class UserVerifyMiddleware(object):
    def process_request(self, request):

        user = request.user
        if request.user.is_authenticated():
            if (not Student.objects.filter(user=user) and not Employer.objects.filter(user=user)):
                if request.method == 'POST': # If the form has been submitted...
                    form = TypeForm(request.POST or None) # A form bound to the POST data
                    if form.is_valid():
                        if form.cleaned_data["user_type"] == "student":
                            new_student = Student.objects.get_or_create(user=user)[0]
                            new_student.save()
                            return None
                        else:
                            new_employer = Employer.objects.get_or_create(user=user)[0]
                            new_employer.save()
                            return None
                else:
                    form = TypeForm(request.POST or None)
                    rotate_token(request)
                    return render(request, 'splashpage/student_or_employer.html', {'form':form})
                    
            else:
                return None
