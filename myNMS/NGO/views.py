from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import studentform,pledgeform
from django.http import HttpResponseRedirect
from .models import pledge

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
def donorview(request):
    donors_list=User.objects.all()
    return render(request,'donorsview.html',{'donor_list':donors_list})
def addstu(request):
    submitted=False
    form=studentform
    if request.method == "POST":
        form=studentform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/addstu?submittted=True')
        else:
            form=studentform
            if 'submitted' in request.GET:
                submitted=True
    
    return render(request,'addstudent.html',{'form':form})

def aple(request):
    submitted=False
    if request.method == "POST":
        form=pledgeform(request.POST)
        if form.is_valid():
            pledgeobj=pledge#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
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