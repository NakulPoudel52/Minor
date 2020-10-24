from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Type,meeting_details,notification
from django.forms.widgets import DateInput,TimeInput


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    Doctor_or_Patient = forms.ChoiceField(
        choices=[(1, "Doctor"), (2, "Patients")],
        required=True
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2',"Doctor_or_Patient"]



class UserAppointmentRequestForm(forms.ModelForm):
    

    class Meta:
        model = meeting_details
        fields = ['date','start_time','end_time','receipt']
        widgets = {
            'date': DateInput(attrs={'type': 'date'}),
            'start_time': TimeInput(attrs={'type':'time'}),
            'end_time':TimeInput(attrs={'type':'time'})
        }
class NotificationForm(forms.ModelForm):

    class Meta:
        model = notification
        fields = ['message_doctor','message_patient']