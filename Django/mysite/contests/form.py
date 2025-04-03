from django import forms
from .models import ContestForm 
from .models import Contest

# Form class for the Contest model
class UserContestSignupForm(forms.ModelForm):
    SEX_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    sex = forms.ChoiceField(choices=SEX_CHOICES)

    class Meta:
        model = ContestForm
        fields = ['name', 'email', 'age', 'sex']


class AdminContestForm(forms.ModelForm):
    class Meta:
        model = Contest
        fields = ['contest_name', 'contest_description', 'pub_date']


