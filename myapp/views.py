from django.shortcuts import render
from django.http import HttpResponse
from .models import notification,disease

# Create your views here.
def home(request):
    if not request.user.is_authenticated:
          return render(request, "users/login.html", {"message": None})
    return render(request,"myapp/index.html")

def appointment(request):
      if not request.user.is_authenticated:
            return render(request, "users/login.html", {"message": None})
       

      name = request.user.username
      to_user = notification.objects.filter(for_user=name,is_view=False)
      context={
            'patients':to_user,
      }
      
      return render(request,"myapp/user.html",context)

def request(request):
      if not request.user.is_authenticated:
            return render(request, "users/login.html", {"message": None})

      context={"user":request.user
      }
      if not request.user.is_staff:
            name = request.POST["nakul"]
            notification.objects.create(to_user=request.user.username,for_user=name)
            return HttpResponse('request send congrats!!')

def search(request):
      disease_name = request.POST["disease"]
      print(disease.objects.filter(Disease__icontains=disease_name)  )
      print(disease_name)
      context={
            'diseaseobj':disease.objects.filter(Disease__icontains=disease_name)  
      }
      return render(request,"myapp/base.html",context)
      