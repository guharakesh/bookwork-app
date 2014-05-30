from django import forms

class TypeForm(forms.Form):
    CHOICES = (
        ('student', 'Student'),
        ('employer', 'Employer')
    )

    user_type = forms.ChoiceField(choices=CHOICES, required=True)

    def __init__(self, *args, **kwargs):
        super(TypeForm, self).__init__(*args, **kwargs)

        self.fields['user_type'].label = "I am a"