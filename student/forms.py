from django import forms
from .models import Student, Skill
from django.contrib.auth.models import User
from itertools import chain
from django.db.models import Q

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['year_in_school','school','skills']

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)


class SkillForm(forms.Form):
    skill_text = forms.CharField(max_length=100)

    def __init__(self, *args, **kwargs):
        super(SkillForm, self).__init__(*args, **kwargs)

        for key in self.fields:
            self.fields[key].required = False

