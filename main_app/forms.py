from django.forms import ModelForm
from .models import contact, Login
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ContactForm(ModelForm):
    class Meta:
        model = contact
        fields = ["name", "email", "mobile_no", "relation"]
        Father = "Father"
        Mother = "Mother"
        Brother = "Brother"
        Sister = "Sister"
        Husband = "Husband"
        Friend = "Friend"
        Relative = "Relative"
        Other = "Other"
        relations = (
            (Father, "Father"),
            (Mother, "Mother"),
            (Brother, "Brother"),
            (Sister, "Sister"),
            (Husband, "Husband"),
            (Friend, "Friend"),
            (Relative, "Relative"),
            (Other, "Other"),
        )
        widgets = {
            "relation": forms.Select(
                choices=relations, attrs={"class": "form-control"}
            ),
        }


class UserCreateForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        label="Email",
        error_messages={"exists": "This Email already exists!"},
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

    def clean_email(self):
        if User.objects.filter(email=self.cleaned_data["email"]).exists():
            raise forms.ValidationError(self.fields["email"].error_messages["exists"])
        return self.cleaned_data["email"]


class LoginForm(ModelForm):
    class Meta:
        model = Login
        fields = ["Username_or_Email", "password"]
        widgets = {
            "password": forms.PasswordInput,
        }
