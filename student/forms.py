from django import forms
from .models import Student, Skill
from django.contrib.auth.models import User
from chosen import forms as chosenforms
from chosen import widgets as chosenwidgets

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['year_in_school','school','skills']

class SkillForm(forms.Form):
    skill_text = forms.CharField(max_length=100)

    def __init__(self, *args, **kwargs):
        super(SkillForm, self).__init__(*args, **kwargs)

        for key in self.fields:
            self.fields[key].required = False

