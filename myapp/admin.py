from django.contrib import admin
from .models import notification,hospital,doctor_profile,Type,schedule

# Register your models here.
class hospitalInline(admin.StackedInline):
    model = hospital.doctors.through
    extra = 1

class doctorAdmin(admin.ModelAdmin):
    inlines = [hospitalInline]

class hospitalAdmin(admin.ModelAdmin):
    filter_horizontal = ("doctors",)



admin.site.register(notification)
#admin.site.register(notification_for_patient)
admin.site.register(hospital,hospitalAdmin)
admin.site.register(doctor_profile,doctorAdmin)
admin.site.register(Type)
admin.site.register(schedule)