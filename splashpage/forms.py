from django import forms
from django.contrib.auth.models import User

class TypeForm(forms.Form):
    user_type = forms.ChoiceField()

    def __init__(self, *args, **kwargs):
        super(TypeForm,self).__init__(*args,**kwargs)

        self.fields['type'].choices = (('student','Student'),('employer','Employer'))
        
