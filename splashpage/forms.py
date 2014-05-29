from django import forms

class TypeForm(forms.Form):
    CHOICES = (
        ('student', 'Student'),
        ('employer', 'Employer')
    )

    user_type = forms.ChoiceField(choices=CHOICES, required=True)

