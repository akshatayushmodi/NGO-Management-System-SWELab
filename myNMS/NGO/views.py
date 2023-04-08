from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages,auth
from django.contrib.auth.models import User
from .forms import studentform,pledgeform
from django.http import HttpResponseRedirect
from datetime import datetime

from .models import pledge,student,totalmoney,estimations,inventory,Donor,expenditure,exphist,Admin

# Create your views here.
def home(request):
    return render(request, 'home.html',{})
def adminlogin(request):
    if request.method == "POST":
        username=str(request.POST['username'])
        password=str(request.POST['password'])
        us=Admin.objects.get(id=1)
        if username==us.username:
            if password==us.password:
                user=authenticate(username=username,password=password)
                if user is not None:
                    user.is_staff=True
                    login(request,user)
                    messages.success(request,"successfully logged in")
                    return render(request,'adminpage.html',{})
                else:
                    messages.success(request,"Please enter correct password or username")
                    return redirect('/adminlogin')
            else:
                messages.success(request,"Please enter correct password")
                return redirect('/adminlogin')
        else:
            messages.success(request,"Please enter correct username")
            return redirect('/adminlogin')
    else:
        if (request.user.is_authenticated and request.user.is_staff):
            return render(request,'adminpage.html',{})
        return render(request,'login_admin.html',{})
def donorlogin(request):
    donor= Donor()
    if request.method == "POST":
        username=str(request.POST['username'])
        password=str(request.POST['password'])
        donor.user=authenticate(username=username,password=password)
        if donor.user is not None:
            login(request,donor.user)
            messages.success(request,"Welcome, you are successfully logged in!!")
            return render(request,'donorpage.html',{})
        else:
            messages.success(request,"Please enter correct username or password ")
            return redirect('donorlogin')
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
        address = request.POST['address']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        
        if password1==password2:
            if User.objects.filter(username = username).exists():
                messages.info(request,'Username Already Taken')
                return redirect('/donorRegistration')
            else:
                donor.user = User.objects.create_user(first_name=first_name,last_name=last_name,email = email_id,username=username,password=password1)
                donor.user.save()
                donor.address=address
                donor.phone=phone_number
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
    donors_list=Donor.objects.all()
    return render(request,'donorsview.html',{'donor_list':donors_list})


def addstu(request):
    if ((request.user.is_authenticated) and (request.user.is_staff)):
        if request.method == 'POST':
            new_student = student()
            new_student.fullname=request.POST['fullname']
            new_student.sclass=request.POST['sclass']
            new_student.familyincome=int(request.POST['familyincome'])
            new_student.moneyneeded=request.POST['moneyneeded']
            if "books" in request.POST:
                new_student.books=request.POST['books']
            if "uniform" in request.POST:
                new_student.uniform=request.POST['uniform']
            new_student.performance=float(request.POST['performance'])
            new_student.gender=request.POST['gender']
            new_student.__score__()
            new_student.save()
            messages.info(request,"Student added!")
            return render(request,'adminpage.html')    
        return render(request,'addstudent.html')

def aple(request):
    if (request.user.is_authenticated):
        submitted=False
        if request.method == "POST":
            form=pledgeform(request.POST)
            if form.is_valid():
                dnr=Donor.objects.filter(user=request.user).first()
                pledgeobj=pledge(money=request.POST['money'],books=request.POST['books'],uniform=request.POST['uniform'],frequency=request.POST['frequency'],donor=dnr,status=False)#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                # pledgeobj.money=form['money']
                # pledgeobj.books=form['books']
                # pledgeobj.uniform=form['uniform']
                # pledgeobj.donor=request.user
                # pledgeobj.status=False
                pledgeobj.time=datetime.now()
                pledgeobj.lastpaid=datetime.now()
                pledgeobj.save()
                messages.info(request,"Pledged!")
                return HttpResponseRedirect('/aple?submittted=True')
        else:
            form=pledgeform
            if 'submitted' in request.GET:
                submitted=True
        return render(request,'addpledge.html',{'form':form})

def pledgeh(request):
    if ((request.user.is_authenticated) and (request.user.is_staff)):
        Semiannually=pledge.objects.filter(frequency="Semiannually")
        Annually=pledge.objects.filter(frequency="Annually")
        for spledge in Semiannually:
            tyet=(datetime.now().month - spledge.time.month) + 12*(datetime.now().year-spledge.time.year)
            tpyet=(spledge.lastpaid.month - spledge.time.month) + 12*(spledge.lastpaid.year-spledge.time.year)
            months=int(tyet)
            month=int(tpyet)
            mon=(months%12)
            monp=(month%12)
            if (mon>6 & monp<=6) | (mon<=6 & monp>6):
                spledge.status=False
        for spledge in Annually:
            tyet=(datetime.now().month - spledge.time.month) + 12*(datetime.now().year-spledge.time.year)
            tpyet=(spledge.lastpaid.month - spledge.time.month) + 12*(spledge.lastpaid.year-spledge.time.year)
            months=int(tyet)
            month=int(tpyet)
            mon=(months%24)
            monp=(month%24)
            if (mon>12 & monp<=12) | (mon<=12 & monp>12):
                spledge.status=False
            
        Pledge_list=pledge.objects.all()
        
        return render(request,'Pledgehistory.html',{'pledgelist':Pledge_list})

def viewdonor(request,donor_id):
    donor = Donor.objects.get(pk=donor_id)
    return render(request,'donorview.html',{'donor':donor})
def clickp(request, pledge_id):
    if ((request.user.is_authenticated) and (request.user.is_staff)):
        Pledge = pledge.objects.get(pk=pledge_id)
        if Pledge.status==False:
            Pledge.status=True
            Pledge.lastpaid=datetime.now()
            money=int(totalmoney.objects.all().count())
            if money>0:
                print(money)
                print("111")
                funds=totalmoney.objects.get(pk=1)
                funds.Sum=int(Pledge.money)+int(funds.Sum)
                funds.save()
            else:
                print("222")
                funds=totalmoney(Sum=int(Pledge.money))
                funds.save()
        else:
            Pledge.status=False
        Pledge.save()
        return render(request,'adminpage.html')
    
    
    
def delstu(request):
    pass
def editest(request):
    if ((request.user.is_authenticated) and (request.user.is_staff)):
        est_list=estimations.objects.all()

        return render(request,'estimates.html',{'estimationlist':est_list})
def changeestimate(request,row_id):
    if ((request.user.is_authenticated) and (request.user.is_staff)):
        row=estimations.objects.get(pk=row_id)
        if request.method == 'POST':
                row.books=request.POST['book']
                row.uniforms=request.POST['uniform']
                row.save()
        return render(request,'est.html',{'row':row})

def vstats(request):
    # inv=inventory.objects.all()
    if ((request.user.is_authenticated) and (request.user.is_staff)):
        stu=student.objects.all()
        money=int(0)
        books=[0,0,0,0,0,0,0,0]
        uniforms=[0,0,0,0,0,0,0,0]
        for stud in stu:
            money=money+int(stud.moneyneeded)
            if stud.books:
                books[stud.sclass]=books[stud.sclass]+1
            if stud.uniform:
                uniforms[stud.sclass]=uniforms[stud.sclass]+1
        for s in range(1,6,1):
            inv=inventory.objects.filter(sclass=s).first()
            if books[s]>0:
                if books[s]>inv.books:
                    books[s]=books[s]-int(inv.books)
                else:
                    books[s]=0
            if uniforms[s]>0:
                if uniforms[s]>inv.uniforms:
                    uniforms[s]=uniforms[s]-int(inv.uniforms)
                else:
                    uniforms[s]=0
            es=estimations.objects.filter(sclass=s).first()
            money=money+books[s]*int(es.books)+uniforms[s]*int(es.uniforms)
        funds=totalmoney.objects.get(pk=1)
        if funds.Sum >= money:
            messages.info(request,"Congrats!! we have enough funds")
        else:
            messages.info(request,"Caution not enough funds!! short by"+ str(money-funds.Sum)+" Rupees" )
        return render(request,'workingstats.html',{'money':money,'totalmoney':funds})

def pref(request):
    
    pass
def minventory(request):
    if ((request.user.is_authenticated) and (request.user.is_staff)):
        inv=inventory.objects.all()
        
        return render(request,'inventoryview.html',{'inventorylist':inv})
def inven(request,inv_id):
    if ((request.user.is_authenticated) and (request.user.is_staff)):
        inv=inventory.objects.get(pk=inv_id)
        if request.method=='POST':
            inv.books=request.POST['book']
            inv.uniforms=request.POST['uniform']
            inv.save()
        return render(request,'inve.html',{'inven':inv})
def updatetexp(request):
    if ((request.user.is_authenticated) and (request.user.is_staff)):
        money=expenditure.objects.all().count()
        if request.method=='POST':
            m=int(request.POST['money'])
            r=request.POST['reason']
            tam=totalmoney.objects.get(pk=1)
            if tam.Sum> m:
                tam.Sum=tam.Sum-int(m)
                tam.save()
            else:
                print("333")
                messages.info(request,'not enough money with NGO')
                return redirect('/addexpend')
            if money>0:
                print("222")
                texp=expenditure.objects.get(pk=1)
                texp.exp=texp.exp+int(m)
                texp.save()
            else:
                print("111")
                texp=expenditure(exp=int(m))
                texp.save()
            t=exphist(expe=int(m),rec=r)
            t.save()
            return redirect('/viewexpenditure')
        return render(request,'update_expenditure.html')

def exph(request):
    if ((request.user.is_authenticated) and (request.user.is_staff)):
        m=expenditure.objects.all().count()
        if m>0:
            expend=exphist.objects.all()
            money=expenditure.objects.get(pk=1)
            return render(request,'expenditurehist.html',{'hist':expend,'total':money})
        else:
            return render(request,'update_expenditure.html')
        
    
    
    
def studentdetails(request):
    students = student.objects.order_by('-score').values()
    inv=inventory.objects.all()
    total=totalmoney.objects.get(id=1).Sum
    
    # for stu in students:
    #     if total>0:
    #         if stu.books:
    #             if  
                
        
    return render(request,'studentlist.html',{'students':students})

def deletestudent(request,student_id):
    if request.method=="GET":
        student.objects.get(id=student_id).delete()
        return redirect(studentdetails)

def modifystudent(request,student_id):
    instance = student.objects.get(id=student_id)
    if request.method == 'POST':
            instance.fullname=request.POST['fullname']
            instance.sclass=request.POST['sclass']
            instance.familyincome=int(request.POST['familyincome'])
            instance.moneyneeded=request.POST['moneyneeded']
            if "books" in request.POST:
                instance.books=request.POST['books']
            if "uniform" in request.POST:
                instance.uniform=request.POST['uniform']
            instance.performance=float(request.POST['performance'])
            instance.gender=request.POST['gender']
            instance.__score__()
            instance.save()
            return redirect(studentdetails)
    return render(request,'modifystudent.html',{'instance':instance,'id':student_id})
    