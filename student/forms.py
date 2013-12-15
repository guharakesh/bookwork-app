from django import forms
from .models import Student
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['year_in_school','school']
