from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class type(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type_data=((1,"Doctor"),(2,"Patients"),(3,"admin"))
    user_type=models.IntegerField(choices=user_type_data,blank=True,null=True)

@receiver(post_save, sender=User)
def create_user_type(sender, instance, created, **kwargs):
    if created:
        type.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_type(sender, instance, **kwargs):
    instance.type.save()


class doctor(models.Model):
    doctor_id = models.OneToOneField(User,on_delete=models.CASCADE,related_name="doctor_intro")
    specialization = models.TextField(max_length=64)
    def __str__(self):
        return f"{self.doctor_id.username},{self.specialization},{self.hospital_id.name}"


class hospital(models.Model):
    name = models.TextField(max_length=200)
    address = models.TextField(max_length=100)
    phone = models.CharField(max_length=10)
    doctors = models.ManyToManyField(doctor,blank=True,related_name="hospitaldoctor")
    def __str__(self):
        return f"{self.name},{self.address}"

class notification_for_doctor(models.Model):
    patients_id = models.ForeignKey(User,on_delete=models.CASCADE)
    doctor_id = models.ForeignKey(doctor,on_delete=models.CASCADE)
    

class notification_for_patient(models.Model):
    patients_id = models.ForeignKey(User,on_delete=models.CASCADE)
    doctor_id = models.ForeignKey(doctor,on_delete=models.CASCADE)
    meeting_id = models.CharField(max_length=25)
    password = models.CharField(max_length=25)
    message = models.TextField(max_length=500)
    start_time = models.DateTimeField( )
    end_time = models.DateTimeField()



# class disease(models.Model):
#     Disease = models.CharField(max_length=64)
#     Precaution_1 = models.CharField(max_length=64,blank=True)
#     Precaution_2 = models.CharField(max_length=64,blank=True)
#     Precaution_3 = models.CharField(max_length=64,blank=True)
#     Precaution_4 = models.CharField(max_length=64,blank=True)

#     def __str__(self):
#         return f"{self.Disease} has precautions as:{self.Precaution_1}..."
    