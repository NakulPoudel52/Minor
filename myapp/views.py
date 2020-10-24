from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
#from .models import notification,disease
from .models import doctor,Type,notification_for_doctor,notification_for_patient,hospital,User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib import messages
from myapp.forms import UserRegisterForm
from django import forms
from django.db import transaction


# Create your views here.
def show_indexpage(request):
      return render(request,"myapp/index.html")
def show_loginpage(request):
      if not request.user.is_authenticated:
            return render(request, "myapp/login.html", {"message": None})

      check = request.user.type.user_type
      print(check)
      if check==1:
            return render(request,'myapp/doctor/doctordashboard.html')
      elif check==2:
            return render(request,'myapp/patients/patientdashboard.html')
      else:
            return HttpResponseRedirect(reverse('admin:index'))


def register(request):
      if request.method == 'POST':
            user_form = UserRegisterForm(request.POST)
            if user_form.is_valid():
                  user = user_form.save()
                  username = user_form.cleaned_data.get('username')
                  user_type = user_form.cleaned_data.get('Doctor_or_Patient')
                  t = Type(user=user,user_type=user_type)
                  t.save()
                  messages.success(request, f'Account created for {username}!')
                  return redirect('do_login')
      else:
            user_form = UserRegisterForm()
      return render(request, "myapp/registration.html", {'user_form': user_form})

def do_login(request):
      username = request.POST["username"]
      password = request.POST["password"]
      user = authenticate(request, username=username, password=password)
      print(user)
      if user is not None:
            login(request, user)
            print('***********')
            check = request.user.type.user_type
            if check==1:
                  return render(request,'myapp/doctor/doctordashboard.html')
            elif check==2:
                  return render(request,'myapp/patients/patientdashboard.html')
            else:
                  return HttpResponseRedirect('admin')
      else:
            return render(request, "myapp/login.html", {"message": "Invalid credentials."})

def logout_view(request):
    logout(request)
    return render(request, "myapp/login.html", {"message": "Logged out."})

def show_register(request):
     return render(request,"myapp/registration.html")
def do_register(request):
      return render(request,"myapp/login.html")
def profile_patient(request):
      context = {}
      return render(request,"myapp/patients/profile.html",context)

def request_appointment(request):
      message = None
      if request.method =='POST':
            doctor_id = request.POST['doctor']
            dtr = doctor.objects.get(pk=doctor_id)
            usr = request.user
            n = notification_for_doctor(doctors=dtr,patients=usr)
            n.save()
            message = True

      doctors = doctor.objects.all()
      hospitals = hospital.objects.all()
      context = {"doctors":doctors,
      "hospitals":hospitals,
      "message":message
      }
      return render(request,"myapp/patients/requestappointment.html",context)


def notification_patient(request):
      info = notification_for_patient.objects.filter(patients=request.user)
      context = {"info":info}
      return render(request,"myapp/patients/notification.html",context)
def notification_doctor(request):
      flag = None
      if request.method=='POST':
            meeting_name = request.POST['Meeting name']
            meeting_password = request.POST['Zoom-Meeting id']
            meeting_id = request.POST['Name']
            date = request.POST['date']
            start_time = request.POST['start time']
            end_time = request.POST['end time']
            message = request.POST['message']
            doctor = request.user.doctor_intro
            print(doctor)
            patient_id = request.POST['patient']
            patient = User.objects.get(pk=patient_id)
            n = notification_for_patient(doctors=doctor,patients=patient,meeting_id=meeting_id,message=message,start_time=start_time,end_time=end_time,meeting_name=meeting_name,password=meeting_password)
            n.save()
            print('done*************************')
            flag = True
            
      n = notification_for_doctor.objects.filter(doctors=request.user.doctor_intro)
      print(n)
      context = {"info":n,
      "flag":flag}
      return render(request,"myapp/doctor/notification.html",context)

# def home(request):
#     if not request.user.is_authenticated:
#           return render(request, "myapp/login.html", {"message": None})
#     return render(request,"myapp/appointment.html")

# def appointment(request):
#       if not request.user.is_authenticated:
#             return render(request, "myapp/login.html", {"message": None})
       

#       name = request.user.username
#       to_user = notification.objects.filter(for_user=name,is_view=False)
#       context={
#             'patients':to_user,
#       }
      
#       return render(request,"myapp/user.html",context)

# def request(request):
#       if not request.user.is_authenticated:
#             return render(request, "users/login.html", {"message": None})

#       context={"user":request.user
#       }
#       if not request.user.is_staff:
#             name = request.POST["nakul"]
#             notification.objects.create(to_user=request.user.username,for_user=name)
#             return HttpResponse('request send congrats!!')

# def search(request):
#       disease_name = request.POST["disease"]
#       print(disease.objects.filter(Disease__icontains=disease_name)  )
#       print(disease_name)
#       context={
#             'diseaseobj':disease.objects.filter(Disease__icontains=disease_name)  
#       }
#       return render(request,"myapp/login.html",context)
      