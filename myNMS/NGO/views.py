from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'home.html',{})
def adminlogin(request):
    if request.method == "POST":
        username=str(request.POST['username'])
        password=str(request.POST['password'])
        if username=="Akshat":
            if password=="Akshat7":
                user=authenticate(username=username,password=password)
                if user is not None:
                    login(request,user)
                return render(request,'adminpage.html',{})
                messages.success(request,"successfully logged in")
            else:
                return redirect('/adminlogin')
    else:
        return render(request,'login_admin.html',{})
def donorlogin(request):
    if request.method == "POST":
        username=str(request.POST['username'])
        password=str(request.POST['password'])
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return render(request,'donorpage.html',{})
            messages.success(request,"successfully logged in")
        else:
            return redirect('/donorlogin')
    else:
        return render(request,'login_donor.html',{})