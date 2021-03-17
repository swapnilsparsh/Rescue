from django.forms import ModelForm
from .models import contact
from django import forms



class ContactForm(forms.ModelForm):
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
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'relation': forms.Select(choices=relations, attrs={'class': 'form-control'}),
        }
