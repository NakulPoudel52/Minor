from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
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


class doctor(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="doctor_intro")
    specialization = models.TextField(max_length=64)
    def __str__(self):
        return f"{self.user.username}{self.specialization}"


class hospital(models.Model):
    name = models.TextField(max_length=200)
    address = models.TextField(max_length=100)
    phone = models.CharField(max_length=10)
    doctors = models.ManyToManyField(doctor,blank=True,related_name="hospitals")
    def __str__(self):
        return f"{self.name},{self.address}"

class meeting_details(models.Model):
    meeting_id = models.CharField(max_length=25,blank =True)
    password = models.CharField(max_length=25,blank =True)
    date = models.DateField(null=True)
    start_time = models.TimeField( null=True)
    end_time = models.TimeField(null=True)
    meeting_name = models.TextField(max_length=50,blank =True)
    receipt = models.ImageField(upload_to = 'images/')

class notification(models.Model):
    patients = models.ForeignKey(User,on_delete=models.CASCADE)
    doctors = models.ForeignKey(doctor,on_delete=models.CASCADE)
    message_doctor = models.TextField(max_length=500,blank=True)
    message_patient = models.TextField(max_length=500,blank=True)
    meeting = models.OneToOneField(meeting_details,on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.patients.username},{self.doctors.user.username}"



# class disease(models.Model):
#     Disease = models.CharField(max_length=64)
#     Precaution_1 = models.CharField(max_length=64,blank=True)
#     Precaution_2 = models.CharField(max_length=64,blank=True)
#     Precaution_3 = models.CharField(max_length=64,blank=True)
#     Precaution_4 = models.CharField(max_length=64,blank=True)

#     def __str__(self):
#         return f"{self.Disease} has precautions as:{self.Precaution_1}..."
    