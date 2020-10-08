from django.contrib import admin
from .models import notification_for_doctor,type,notification_for_patient,hospital,doctor

# Register your models here.
admin.site.register(notification_for_doctor)
admin.site.register(notification_for_patient)
admin.site.register(hospital)
admin.site.register(doctor)
admin.site.register(type)
