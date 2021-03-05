from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
import datetime
import json
from psycopg2.extras import DateRange, DateTimeTZRange, NumericRange, Range
from django.contrib.postgres import forms, lookups
from multiselectfield import MultiSelectField
from PIL import Image

#from .utils import AttributeSetter
__all__ = [
    'RangeField', 'IntegerRangeField', 'BigIntegerRangeField',
    'DecimalRangeField', 'DateTimeRangeField', 'DateRangeField',
    'FloatRangeField',
]

# Create your models here.
#address,phone,profile pic
class Type(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='type')
    user_type_data=((1,"Doctor"),(2,"Patients"),(3,"admin"))
    user_type=models.IntegerField(choices=user_type_data,blank=True,null=False)

    def __str__(self):
        return f"{self.user.username} is {self.user_type}"

# @receiver(post_save, sender=User)
# def create_user_type(sender, instance, created, **kwargs):
#     if created:
#         Type.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_type(sender, instance, **kwargs):
#     instance.type.save()

#payment_details,NMC_ID,which_hospitals,notes,timing,feesdetail
class doctor_profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="doctor_intro")
    profile_pic = models.ImageField(default='default.jpg', upload_to='profile_pics')
    specialization = models.TextField(max_length=64)
    payment_details = models.TextField(max_length=64,blank=True)
    NMC_ID = models.IntegerField(blank=True,null=True,default=0)
    feesdetail = models.IntegerField(blank=True,default=500)
    wallet = models.IntegerField(default=1000,null=True,blank=True)
    def save(self):
        super().save()

        img = Image.open(self.profile_pic.path)

        if img.height > 400 or img.width > 450:
            output_size = (400, 450)
            img.thumbnail(output_size)
            img.save(self.profile_pic.path)

    def __str__(self):
        return f"{self.user.username}{self.specialization}"

DAYS_OF_WEEK = (
    (1, 'Sunday'),
    (2, 'Monday'),
    (3, 'Tuesday'),
    (4, 'Wednesday'),
    (5, 'Thursday'),
    (6, 'Friday'),
    (7, 'Saturday'),
    
)

class schedule(models.Model):
    DAYS_OF_WEEK = (
    (1, 'Sunday'),
    (2, 'Monday'),
    (3, 'Tuesday'),
    (4, 'Wednesday'),
    (5, 'Thursday'),
    (6, 'Friday'),
    (7, 'Saturday'),)
    

    day = models.IntegerField( choices=DAYS_OF_WEEK)
    StartTime = models.TimeField(null=True,blank=True )
    BreakStartTime = models.TimeField(null=True,blank=True )
    BreakEndTime = models.TimeField(null=True,blank=True )
    EndTime = models.TimeField(null=True,blank=True)
    doctor = models.ForeignKey(doctor_profile,on_delete=models.CASCADE,related_name='timing')



class patients_profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="patient_intro")
    profile_pic = models.ImageField(default='default.jpg', upload_to='profile_pics')
    wallet = models.IntegerField(default=1000,null=True,blank=True)
    def save(self):
        super().save()

        img = Image.open(self.profile_pic.path)

        if img.height > 300 or img.width > 400:
            output_size = (400, 450)
            img.thumbnail(output_size)
            img.save(self.profile_pic.path)

class Monitoring(models.Model):
    value1 = models.PositiveIntegerField()
    value2 = models.PositiveIntegerField(blank=True,null=True)
    subject = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    patient = models.ForeignKey(patients_profile,on_delete=models.CASCADE,related_name="monitor",null=True,blank=True)

class hospital(models.Model):
    name = models.TextField(max_length=200)
    address = models.TextField(max_length=100)
    phone = models.CharField(max_length=10)
    doctors = models.ManyToManyField(doctor_profile,blank=True,related_name="hospitals")
    picture  = models.ImageField(default='hospital.jpg',upload_to = 'hospital')
    def __str__(self):
        return f"{self.name},{self.address}"

class meeting_details(models.Model):
    meeting_id = models.CharField(max_length=25,blank =True)
    password = models.CharField(max_length=25,blank =True)
    date = models.DateField(null=True)
    start_time = models.TimeField( null=True)
    end_time = models.TimeField(null=True)
    meeting_name = models.TextField(max_length=50,blank =True)
    

class notification(models.Model):
    patients = models.ForeignKey(patients_profile,on_delete=models.CASCADE)
    doctors = models.ForeignKey(doctor_profile,on_delete=models.CASCADE,related_name="meetings")
    message_doctor = models.TextField(max_length=500,blank=True)
    message_patient = models.TextField(max_length=500,blank=True)
    meeting = models.OneToOneField(meeting_details,on_delete=models.CASCADE,related_name="meeting_detail")
    timestamp = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.patients.user.username},{self.doctors.user.username}"





# class disease(models.Model):
#     Disease = models.CharField(max_length=64)
#     Precaution_1 = models.CharField(max_length=64,blank=True)
#     Precaution_2 = models.CharField(max_length=64,blank=True)
#     Precaution_3 = models.CharField(max_length=64,blank=True)
#     Precaution_4 = models.CharField(max_length=64,blank=True)

#     def __str__(self):
#         return f"{self.Disease} has precautions as:{self.Precaution_1}..."
    