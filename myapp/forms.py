from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Type


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    Doctor_or_Patient = forms.ChoiceField(
        choices=[(1, "Doctor"), (2, "Patients")],
        required=True
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2',"Doctor_or_Patient"]
