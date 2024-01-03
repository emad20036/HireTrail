# forms.py in your 'job' app

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User





class CreateUserForm(UserCreationForm):

    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            'class': "form-control",
            'placeholder': 'Enter your password'
        })
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={
            'class': "form-control",
            'placeholder': 'Confirm your password'
        })

    )
 






    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Enter your username',
                'id': 'username'
            }),
            'first_name': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Enter your first name',
                'id': 'firstName'
            }),
            'last_name': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Enter your last name',
                'id': 'lastName'
            }),
            'email': forms.EmailInput(attrs={
                'class': "form-control",
                'placeholder': 'Enter your email',
                'id': 'email'
            }),
        }
# forms.py in your 'job' app

from django import forms
from .models import Job
from .models import Person

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['company', 'position', 'status', 'job_location', 'job_type']
        widgets = {
            'company': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Enter the company name',
            }),
            'position': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Enter the position',
            }),
            'status': forms.Select(attrs={
                'class': "form-control",
            }),
            'job_location': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Enter the job location',
            }),
            'job_type': forms.Select(attrs={
                'class': "form-control",
            }),
        }
# class ProfileForm(forms.ModelForm): 
#     class Meta:
#         model = Person
#         fields = ['fname', 'lname', 'username', 'email',]
      