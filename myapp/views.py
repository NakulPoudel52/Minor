from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
#from .models import notification,disease
from .models import doctor_profile,Type,notification,hospital,User,schedule,patients_profile,meeting_details
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib import messages
from myapp.forms import UserRegisterForm,UserAppointmentRequestForm,NotificationForm,DoctorProfileForm,HospitalForm,ScheduleForm,PatientProfileForm,AckForm
from django import forms
from django.db import transaction
import datetime
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.postgres.search import TrigramDistance,TrigramSimilarity

# Create your views here.
def show_indexpage(request):
      return render(request,"myapp/index.html")
def show_loginpage(request):
      if not request.user.is_authenticated:
            return render(request, "myapp/login.html", {"message": None})

      check = request.user.type.user_type
      print(check)
      if check==1:
            return render(request,'myapp/doctor/doctordashboard.html',{'wallet':request.user.doctor_intro.wallet})
      elif check==2:
            return render(request,'myapp/patients/patientdashboard.html',{'wallet':request.user.patient_intro.wallet})
            print(request.user.patient_intro.wallet)
      else:
            return HttpResponseRedirect(reverse('admin:index'))


def register(request):
      if request.method == 'POST':
            user_form = UserRegisterForm(request.POST)
            if user_form.is_valid():
                  username = user_form.cleaned_data.get('username')
                  user_type = user_form.cleaned_data.get('Doctor_or_Patient')
                  print(user_type)
                  user = user_form.save()
                  t = Type(user=user,user_type=user_type)
                  t.save()
                  messages.success(request, f'Account created for {username}!',extra_tags='text-white')
                  return redirect('show_login')
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
            check = request.user.type.user_type
            if check==1:
                  if not doctor_profile.objects.filter(user=request.user).first():
                        print('**********************************************')
                        doctor_profile(user = request.user).save()
                  return render(request,'myapp/doctor/doctordashboard.html',{'wallet':request.user.doctor_intro.wallet})
            elif check==2:
                  if not patients_profile.objects.filter(user=request.user).first():
                        patients_profile(user = request.user).save()
                  return render(request,'myapp/patients/patientdashboard.html',{'wallet':request.user.patient_intro.wallet})
            else:
                  return HttpResponseRedirect('admin')
      else:
            return render(request, "myapp/login.html", {"message": "Invalid credentials."})

def logout_view(request):
    logout(request)
    return render(request,"myapp/index.html")

def show_register(request):
     return render(request,"myapp/registration.html")
def do_register(request):
      return render(request,"myapp/login.html")
def profile_doctor(request):
      if request.method == 'POST':
            d_form = DoctorProfileForm(request.POST,request.FILES,instance=request.user.doctor_intro,)
            if d_form.is_valid:
                  d_form.save()
            return redirect('profile_doctor')
      d_form = DoctorProfileForm(instance=request.user.doctor_intro)
      sdl = schedule.objects.all().filter(doctor = request.user.doctor_intro)
      #h_form = HospitalForm()
      context = {'d_form':d_form,
                  'schedule':sdl,
                  'days':['sunday','monday','tuesday','wednesday','thursday','Friday','saturday'],}      
      return render(request,"myapp/doctor/profile.html",context)

def scheduler(request):
      if request.method == 'POST':
            s_form = ScheduleForm(request.POST)
            time = request.POST["StartTime"]
            starttime = (s_form['StartTime'].value())+':00'
            breakstarttime = (s_form['BreakStartTime'].value())+':00'
            breakendtime = (s_form['BreakEndTime'].value())+':00'
            endtime = (s_form['EndTime'].value())+':00'

            
            if  breakstarttime == ':00':
                  stime = datetime.datetime.strptime(starttime, '%H:%M:%S')
                  etime = datetime.datetime.strptime(endtime, '%H:%M:%S')
                  update_request = request.POST.copy()
                  update_request.update({'StartTime': stime.time(),'EndTime':etime.time()})
            else:
                  stime = datetime.datetime.strptime(starttime, '%H:%M:%S')
                  etime = datetime.datetime.strptime(endtime, '%H:%M:%S')
                  bstime = datetime.datetime.strptime(breakstarttime, '%H:%M:%S')
                  betime = datetime.datetime.strptime(breakendtime, '%H:%M:%S')
                  update_request = request.POST.copy()
                  update_request.update({'StartTime': stime.time(),'BreakStartTime':bstime.time(),'BreakEndTime':betime.time(),'EndTime':etime.time()})
            
            s_form = ScheduleForm(update_request)
            print(s_form)
            day = int(request.POST["day"])
            print('***********************')
            print(day)
            s_form.errors
            if s_form.is_valid():
                  print('********************************')
                  start_time = s_form.cleaned_data.get('StartTime')
                  break_start_time =s_form.cleaned_data.get('BreakStartTime')
                  break_end_time = s_form.cleaned_data.get('BreakEndTime')
                  end_time = s_form.cleaned_data.get('EndTime')

                  if not (schedule.objects.filter(day=day,doctor=request.user.doctor_intro)):
                        s = schedule(day=day,StartTime=start_time,BreakStartTime=break_start_time,BreakEndTime=break_end_time,EndTime=end_time,doctor=request.user.doctor_intro)
                        s.save()
                        print(start_time,break_start_time,break_end_time,end_time)
                  else:
                        s = schedule.objects.filter(day=day,doctor=request.user.doctor_intro)
                        # s.StartTime = start_time
                        # s.BreakEndTime = break_end_time
                        # s.BreakStartTime = break_start_time
                        # s.EndTime = end_time
                        s.update(StartTime=start_time,BreakStartTime=break_start_time,BreakEndTime=break_end_time,EndTime=end_time)

            print(s_form.cleaned_data)
            print(s_form.errors.as_data())
            return redirect('schedule')


      s_form = ScheduleForm()
      context = {'s_form':s_form,'days':['sunday','monday','tuesday','wednesday','thursday','Friday','saturday']}
      return render(request,"myapp/doctor/schedule.html",context)
def profile_patient(request):
      if request.method == 'POST':
            p_form = PatientProfileForm(request.POST,request.FILES,instance=request.user.patient_intro,)
            if p_form.is_valid:
                  p_form.save()
            return redirect('profile_patient')
      p_form = PatientProfileForm(instance=request.user.patient_intro)
      
      #h_form = HospitalForm()
      context = {'p_form':p_form,
                  
                  'days':['sunday','monday','tuesday','wednesday','thursday','Friday','saturday'],}      
      
      return render(request,"myapp/patients/profile.html",context)



def request_appointment(request):
      message = None
      if request.method == 'POST':
            print(request.POST["doctor"])
            
            did = int(request.POST["doctor"])
            request_appointment_form = UserAppointmentRequestForm(request.POST,request.FILES)
            notification_form = NotificationForm(request.POST)
            if request_appointment_form.is_valid() and notification_form.is_valid():
                  print(request_appointment_form.errors)
                  print('*************************************')
                  print(notification_form.errors)
                  ra = request_appointment_form.save()
                  n=notification_form.save(commit=False)
                  
                  
                  dtr = doctor_profile.objects.get(pk=did)
                  n.doctors = dtr
                  n.patients = request.user.patient_intro
                  n.meeting = ra
                  n.save()

                  message = True
            return redirect('request_appointment')
      
                  # usr = request.user
                  # n(doctors=dtr,patients=usr).save()
            
            print('*************************************')
            print(notification_form.errors)     
      
      request_appointment_form = UserAppointmentRequestForm()
      notification_form = NotificationForm()
      doctorlist = doctor_profile.objects.all()
      page = request.GET.get('page', 1)

      paginator = Paginator(doctorlist, 2)
      try:
            doctors = paginator.page(page)
      except PageNotAnInteger:
            doctors = paginator.page(1)
      except EmptyPage:
            doctors = paginator.page(paginator.num_pages)

      hospitals = hospital.objects.all()
      sdl = schedule.objects.all()
      context = {"doctors":doctors,
      "hospitals":hospitals,
      "message":message,
      "request_appointment_form":request_appointment_form,
      "notification_form":notification_form,
      'days':['sunday','monday','tuesday','wednesday','thursday','Friday','saturday'],
      'schedule':sdl,
      }
      return render(request,"myapp/patients/requestappointment.html",context)


def notification_patient(request):
      info = notification.objects.filter(patients=request.user)

      context = {"info":info}
      return render(request,"myapp/patients/notification.html",context)
def notify(request):
      flag = None
      if request.method=='POST':
            pid = int(request.POST["patient"])
            print('*************************************')

            print(pid)
            a_frm = AckForm(request.POST)
            n_frm = NotificationForm(request.POST)
            if a_frm.is_valid() and n_frm.is_valid():
                  meeting_name=a_frm.cleaned_data.get('meeting_name')
                  meeting_id=a_frm.cleaned_data.get('meeting_id')
                  password=a_frm.cleaned_data.get('password')
                  message_patient=n_frm.cleaned_data.get('message_patient')
                  
                  print(meeting_name)
                  # ntf = a_frm.save()
                  pt = patients_profile.objects.get(pk=pid)
                  ntf =notification.objects.filter(patients=pt,doctors=request.user.doctor_intro,read=False).first()
                  ntf.meeting_name = meeting_name
                  #n = meeting_details(meeting_id=meeting_id,password=password)
                  x=ntf.meeting.id
                  mn = meeting_details.objects.get(pk=x)
                  mn.meeting_id = meeting_id
                  mn.password = password
                  mn.meeting_name = meeting_name
                  mn.save()
                  ntf.message_patient = message_patient
                  ntf.read = True
                  ntf.save()
            return redirect('notification_doctor')
            # print(doctor)
            # patient_id = request.POST['patient']
            # patient = User.objects.get(pk=patient_id)
            # n = notification(doctors=doctor,patients=patient,meeting_id=meeting_id,message=message,start_time=start_time,end_time=end_time,meeting_name=meeting_name,password=meeting_password)
            # n.save()
            # print('done*************************')
            # flag = True
            
      n = notification.objects.all().filter(doctors=request.user.doctor_intro)
      print(n)
      a_form = AckForm()
      context = {"info":n,
      "flag":flag,
      'a_form':a_form,
      'n_form':NotificationForm()}
      return render(request,"myapp/doctor/notification.html",context)
def appointment_status(request):
      n = notification.objects.all().filter(patients=request.user.patient_intro).order_by('-timestamp')
      context = {'status':n}
      return render(request,'myapp/patients/appointmentstatus.html',context)



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

def search_doctors(request):
      message = None
      if request.method == 'POST'  :
            print(request.POST["doctor"])
            
            did = int(request.POST["doctor"])
            request_appointment_form = UserAppointmentRequestForm(request.POST,request.FILES)
            notification_form = NotificationForm(request.POST)
            if request_appointment_form.is_valid() and notification_form.is_valid():
                  print(request_appointment_form.errors)
                  print('*************************************')
                  print(notification_form.errors)
                  ra = request_appointment_form.save()
                  n=notification_form.save(commit=False)
                  
                  
                  dtr = doctor_profile.objects.get(pk=did)
                  n.doctors = dtr
                  n.patients = request.user.patient_intro
                  n.meeting = ra
                  n.save()

                  message = True
            return redirect('request_appointment')
      
                  # usr = request.user
                  # n(doctors=dtr,patients=usr).save()
            
            print('*************************************')
            print(notification_form.errors)     
      
      request_appointment_form = UserAppointmentRequestForm()
      notification_form = NotificationForm()
      doctor_name = request.GET["test"]
      #print(disease.objects.filter(Disease__icontains=disease_name)  )
      d = User.objects.annotate(similarity=TrigramSimilarity('username',doctor_name ),).filter(similarity__gt=0.2).order_by('-similarity')
      print(doctor_name)
      doctorlist = doctor_profile.objects.filter(user__in =d) 
      #doctorlist = doctor_profile.objects.all()
      page = request.GET.get('page', 1)

      paginator = Paginator(doctorlist, 2)
      try:
            doctors = paginator.page(page)
      except PageNotAnInteger:
            doctors = paginator.page(1)
      except EmptyPage:
            doctors = paginator.page(paginator.num_pages)

      hospitals = hospital.objects.all()
      sdl = schedule.objects.all()
      context = {"doctors":doctors,
      "hospitals":hospitals,
      "message":message,
      "request_appointment_form":request_appointment_form,
      "notification_form":notification_form,
      'days':['sunday','monday','tuesday','wednesday','thursday','Friday','saturday'],
      'schedule':sdl,
      }
      return render(request,"myapp/patients/requestappointment.html",context)
#User.objects.annotate(similarity=TrigramSimilarity('username', test),).filter(similarity__gt=0.3).order_by('-similarity')