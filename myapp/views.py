from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
#from .models import notification,disease
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse



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

def do_login(request):
      username = request.POST["username"]
      password = request.POST["password"]
      user = authenticate(request, username=username, password=password)
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
      context = {}
      return render(request,"myapp/patients/requestappointment.html",context)


def notification_patient(request):
      context = {}
      return render(request,"myapp/patients/notification.html",context)


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
      