from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Type,meeting_details,notification,doctor_profile,hospital,schedule,patients_profile
from django.forms.widgets import DateInput,TimeInput
from multiselectfield import MultiSelectField
from django.core.exceptions import ValidationError
from datetime import datetime, date,timedelta

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
        fields = ['date','start_time','end_time']
        widgets = {
            'date': DateInput(attrs={'type': 'date'}),
            'start_time': TimeInput(attrs={'type':'time'}),
            'end_time':TimeInput(attrs={'type':'time'})
        }
    def clean(self):
        cleaned_data = super().clean()
        date  = cleaned_data.get('date')
        start_time = cleaned_data.get('start_time')
        end_time = cleaned_data.get('end_time')
        dtr = cleaned_data.get('doctor')
        print('**********************************')
        print(type(start_time))
        print(start_time)
        print(type(datetime.combine(date.today(), end_time) - datetime.combine(date.today(), start_time)))
        #0:50:00
        elapsed = datetime.combine(date.today(), end_time) - datetime.combine(date.today(), start_time)
        if elapsed > timedelta(minutes=30):
            raise forms.ValidationError('Time period must be less than 30 minute')




class NotificationForm(forms.ModelForm):

    class Meta:
        model = notification
        fields = ['message_doctor','message_patient']

class AckForm(forms.ModelForm):

    class Meta:
        model = meeting_details
        fields = ['meeting_name','meeting_id','password']

class PatientProfileForm(forms.ModelForm):

    class Meta:
        model = patients_profile
        fields = ['profile_pic']

class DoctorProfileForm(forms.ModelForm):

    class Meta:
        model = doctor_profile
        fields = ['profile_pic','specialization','NMC_ID','payment_details']
    # hopitals = forms.ModelMultipleChoiceField(queryset=hospital.objects.all())

    # def __init__(self, *args, **kwargs):
    #     # Only in case we build the form from an instance
    #     # (otherwise, 'toppings' list should be empty)
    #     if kwargs.get('instance'):
    #         # We get the 'initial' keyword argument or initialize it
    #         # as a dict if it didn't exist.
    #         initial = kwargs.setdefault('initial', {})
    #         # The widget for a ModelMultipleChoiceField expects
    #         # a list of primary key for the selected data.
    #         initial['hospitals'] = [t.pk for t in 
    #             kwargs['instance'].hospital_set.all()]

    #     forms.ModelForm.__init__(self, *args, **kwargs)

    # # Overriding save allows us to process the value of 'toppings' field
    # def save(self, commit=True):
    #     # Get the unsaved Pizza instance
    #     instance = forms.ModelForm.save(self, False)

    #     # Prepare a 'save_m2m' method for the form,
    #     old_save_m2m = self.save_m2m

    #     def save_m2m():
    #         old_save_m2m()
    #         # This is where we actually link the pizza with toppings
    #         instance.hospital_set.clear()
    #         for hospital in self.cleaned_data['hospitals']:
    #             instance.hospital_set.add(course)

    #     self.save_m2m = save_m2m

    #     # Do we need to save all changes now?
    #     #if commit:
    #     instance.save()
    #     self.save_m2m()

    #     return instance

class HospitalForm(forms.ModelForm):

    class Meta:
        model = hospital
        fields = ['doctors']
valid_time_formats = ['%H:%M %p', '%I:%M%p', '%I:%M %p']
class ScheduleForm(forms.Form):
    DAYS_OF_WEEK = [
    (0, 'Sunday'),
    (1, 'Monday'),
    (2, 'Tuesday'),
    (3, 'Wednesday'),
    (4, 'Thursday'),
    (5, 'Friday'),
    (6, 'Saturday'),]
    #day = forms.ChoiceField( choices=DAYS_OF_WEEK)
    StartTime = forms.TimeField(widget=TimeInput(attrs={'class': 'time-pick','type':'time'},format='%H:%M:%S'),help_text='ex: 10:30:00',input_formats='%H:%M:%S')
    BreakStartTime = forms.TimeField(widget=TimeInput(attrs={'class': 'time-pick','type':'time'}),input_formats='%H:%M:%S',required=False)
    BreakEndTime = forms.TimeField(widget=TimeInput(attrs={'class': 'time-pick','type':'time'}),input_formats='%H:%M:%S',required=False)
    EndTime = forms.TimeField(widget=TimeInput(attrs={'class': 'time-pick','type':'time'}),input_formats='%H:%M:%S')

    class Meta:
        model = schedule
        fields = ['StartTime','BreakStartTime','BreakEndTime','EndTime']
        # widgets = {
        #     #'date': DateInput(attrs={'type': 'date'}),
        #     'StartTime': TimeInput(attrs={'class':'time-pick'}),
        #     'BreakStartTime': TimeInput(attrs={'type':'time'}),
        #     'BreakEndTime': TimeInput(attrs={'type':'time'}),
        #     'EndTime':TimeInput(attrs={'type':'time'})
        # }