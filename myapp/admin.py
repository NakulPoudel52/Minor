from django.contrib import admin
from .models import notification_for_doctor,Type,notification_for_patient,hospital,doctor

# Register your models here.
class hospitalInline(admin.StackedInline):
    model = hospital.doctors.through
    extra = 1

class doctorAdmin(admin.ModelAdmin):
    inlines = [hospitalInline]

class hospitalAdmin(admin.ModelAdmin):
    filter_horizontal = ("doctors",)



admin.site.register(notification_for_doctor)
admin.site.register(notification_for_patient)
admin.site.register(hospital,hospitalAdmin)
admin.site.register(doctor,doctorAdmin)
admin.site.register(Type)
