from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import doctor_profile,schedule


# @receiver(post_save, sender=doctor_profile)
# def create_schedule(sender, instance, created, **kwargs):
#      if created:
#         print('****************************')
#         print(instance)
        
        

# @receiver(post_save, sender=doctor_profile)
# def save_schedule(sender, instance, **kwargs):
#     print(instance) 
#     instance.schedule.save()