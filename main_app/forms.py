from django.forms import ModelForm
from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm




class ContactForm(ModelForm):
    class Meta:
        model = contact
        fields = ['name', 'email', 'relation']
        Father = 'Father'
        Mother = 'Mother'
        Brother = 'Brother'
        Sister = 'Sister'
        Husband = 'Husband'
        Friend = 'Friend'
        Relative = 'Relative'
        Other = 'Other'
        relations = (
            (Father, 'Father'),
            (Mother, 'Mother'),
            (Brother, 'Brother'),
            (Sister, 'Sister'),
            (Husband, 'Husband'),
            (Friend, 'Friend'),
            (Relative, 'Relative'),
            (Other, 'Other'),
        )
        widgets = {
            'relation': forms.Select(choices=relations, attrs={'class': 'form-control'}),
        }

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone_number', 'image','about_me']