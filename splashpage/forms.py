from django import forms
from django.contrib.auth.models import User

class TypeForm(forms.Form):
    type = forms.ChoiceField()
    self.fields['type'].choices = (('student','Student'),('employer','Employer'))
