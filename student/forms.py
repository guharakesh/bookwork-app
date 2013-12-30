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
        fields = ['year_in_school','school']

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        widgets = {
            'skill_text': chosenwidgets.ChosenSelectMultiple(),
        }
