from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout

from django.contrib import messages,auth
from django.contrib.auth.models import User
from .forms import studentform,pledgeform
from django.http import HttpResponseRedirect
from .models import pledge,student,Donor



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
                return redirect('adminlogin')
    else:
        return render(request,'login_admin.html',{})
def donorlogin(request):
    donor = Donor()
    if request.method == "POST":
        username=str(request.POST['username'])
        password=str(request.POST['password'])
        donor.user=authenticate(username=username,password=password)
        if donor.user is not None:
            login(request,donor.user)
            return render(request,'donorpage.html',{})
            messages.success(request,"successfully logged in")
        else:
            return redirect('/donorlogin')
    else:
        return render(request,'login_donor.html',{})


def donorRegistration(request):
    donor = Donor()
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
                return redirect('/donorRegistration')
            else:
                donor.user = User.objects.create_user(first_name=first_name,last_name=last_name,email = email_id,username=username,password=password1)
                user.save()
                donor.save()
                messages.info(request,'User created')
                return redirect('/')

        else:
            messages.info(request,'Password does not match')
            return redirect('/donorRegistration')
    
    else:
        return render(request,'register_donor.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def donorview(request):
    donors_list=User.objects.all()
    return render(request,'donorsview.html',{'donor_list':donors_list})


def addstu(request):
    new_student = student()
    if request.method == 'POST':
        new_student.fullname=request.POST['fullname']
        new_student.sclass=request.POST['sclass']
        new_student.familyincome=request.POST['familyincome']
        new_student.moneyneeded=request.POST['moneyneeded']
        new_student.books=request.POST['books']
        new_student.uniform=request.POST['uniform']
        new_student.performance=request.POST['performance']
        new_student.gender=request.POST['gender']

        new_student.save()
        return redirect('/adminpage.html')    
    return render(request,'addstudent.html')

def aple(request):
    submitted=False
    if request.method == "POST":
        form=pledgeform(request.POST)
        if form.is_valid():
            pledgeobj=pledge()#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            pledgeobj.money=form['money']
            pledgeobj.books=form['books']
            pledgeobj.uniform=form['uniform']
            pledgeobj.donor=request.user
            pledgeobj.status=False
            pledgeobj.save()
            return HttpResponseRedirect('/aple?submittted=True')
    else:
        form=pledgeform
        if 'submitted' in request.GET:
            submitted=True
    return render(request,'addpledge.html',{'form':form})

def pledgeh(request, pledge_id):
    # Pledge=pledge.objects.get(pk=pledge_id)
    pass
def delstu(request):
    pass
def editest(request):
    pass
def vstats(request):
    pass
def pref(request):
    pass
def minventory(request):
    pass

