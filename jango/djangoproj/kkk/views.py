from django.shortcuts import render,redirect
from django.http import HttpResponse
from datetime import datetime
from kkk.models import kkkModel
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.

def home(request):
    serverTime=datetime.now()
    # return HttpResponse("<h1>Home page</h1>")
    #return render(request,"home.html",{'urrentTIme':serverTime})
    todos=kkkModel.objects.all()
    return render(request,"home.html",{'todos':todos})
    

def about(request):
    #return HttpResponse("<h1>About page</h1>")
    return render(request,"about.html")

def add(request):
    #return HttpResponse("<h1>About page</h1>")
    #n1 = int(request.GET["num1"])
    #n2 = int(request.GET["num2"])
    n1 = int(request.POST["num1"])
    n2 = int(request.POST["num2"])
    result = n1+n2
    return render(request,'add.html',{"result":result})

def register(request):
    form=UserCreationForm()
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            #get username from dictionary
            username=form.cleaned_data.get('username')
            messages.success(request,"Account created for {}!".format(username))
            return redirect('/')
        else:
            form=UserCreationForm()
    return render(request,'register.html',{'form':form})
