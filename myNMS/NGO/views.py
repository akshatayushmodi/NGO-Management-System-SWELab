from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User 

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

def donorRegistration(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email_id = request.POST['email_id']
        phone_number = request.POST['phone_number']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        
        if password1==password2:
            if User.objects.filter(username = username).exists():
                messages.info(request,'Username Taken')
                return redirect(reverse('register_donor'))
            else:
                user = User.objects.create_user(first_name=first_name,last_name=last_name,email_id = email_id,phone_number=phone_number,username=username,password=password1)
                user.save()
                messages.info(request,'User created')
                return redirect('/')

        else:
            messages.info(request,'Password does not match')
            return redirect(reverse('register_donor'))
    
    else:
        return render(request,'register_donor.html')