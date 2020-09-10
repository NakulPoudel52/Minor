from django.urls import path

from . import views

urlpatterns = [
   path("home/",views.home,name="home"),
   path("appointment/",views.appointment,name="appointment"),
   path("request",views.request,name="request"),
   path("search/",views.search,name="search"),
]