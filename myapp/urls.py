from django.urls import path
from . import views

urlpatterns = [
   path("", views.show_indexpage, name="index"),
   path("login", views.show_loginpage, name="show_login"),
   path("dologin", views.do_login, name="do_login"),
   path("logout", views.logout_view, name="logout"),
   path("register", views.register, name="register"),
   path("doregister", views.do_register, name="do_register"),
   path("profilepatient",views.profile_patient,name="profile_patient"),
   path("profiledoctor",views.profile_doctor,name="profile_doctor"),
   path("requestappointment/",views.request_appointment,name="request_appointment"),
   path("notificationpatient",views.notification_patient,name="notification_patient"),
   path("doctor/notification",views.notification_doctor,name="notification_doctor"),
   path("doctor/schedule",views.scheduler,name="schedule")
   
   #path("search/",views.search,name="search"),
]