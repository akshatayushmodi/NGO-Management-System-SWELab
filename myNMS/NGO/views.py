from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages,auth
from django.contrib.auth.models import User
from .forms import studentform,pledgeform
from django.http import HttpResponseRedirect

from .models import pledge,student,totalmoney,estimations,inventory,Donor,expenditure,exphist

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
                    user.is_staff=True
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
        address = request.POST['address']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        
        if password1==password2:
            if User.objects.filter(username = username).exists():
                messages.info(request,'Username Taken')
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
            return render(request,'adminpage.html')    
        return render(request,'addstudent.html')

def aple(request):
    submitted=False
    if request.method == "POST":
        form=pledgeform(request.POST)
        if form.is_valid():
            dnr=Donor.objects.filter(user=request.user).first()
            pledgeobj=pledge(money=request.POST['money'],books=request.POST['books'],uniform=request.POST['uniform'],donor=dnr,status=False)#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            # pledgeobj.money=form['money']
            # pledgeobj.books=form['books']
            # pledgeobj.uniform=form['uniform']
            # pledgeobj.donor=request.user
            # pledgeobj.status=False
            pledgeobj.save()
            return HttpResponseRedirect('/aple?submittted=True')
    else:
        form=pledgeform
        if 'submitted' in request.GET:
            submitted=True
    return render(request,'addpledge.html',{'form':form})

def pledgeh(request):
    Pledge_list=pledge.objects.all()
    
    return render(request,'Pledgehistory.html',{'pledgelist':Pledge_list})

def viewdonor(request,donor_id):
    donor = Donor.objects.get(pk=donor_id)
    return render(request,'donorview.html',{'donor':donor})
def clickp(request, pledge_id):
    Pledge = pledge.objects.get(pk=pledge_id)
    if Pledge.status==False:
        Pledge.status=True
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
    est_list=estimations.objects.all()

    return render(request,'estimates.html',{'estimationlist':est_list})
def changeestimate(request,row_id):
    row=estimations.objects.get(pk=row_id)
    if request.method == 'POST':
            row.books=request.POST['book']
            row.uniforms=request.POST['uniform']
            row.save()
    return render(request,'est.html',{'row':row})

def vstats(request):
    # inv=inventory.objects.all()
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
    return render(request,'workingstats.html',{'money':money,'totalmoney':funds})

def pref(request):
    
    pass
def minventory(request):
    inv=inventory.objects.all()
    
    return render(request,'inventoryview.html',{'inventorylist':inv})
def inven(request,inv_id):
    inv=inventory.objects.get(pk=inv_id)
    if request.method=='POST':
        inv.books=request.POST['book']
        inv.uniforms=request.POST['uniform']
        inv.save()
    return render(request,'inve.html',{'inven':inv})
def updatetexp(request):
    money=expenditure.objects.all().count()
    if request=='POST':
        m=request.POST['money']
        r=request.POST['reason']
        tam=totalmoney.objects.get(pk=1)
        if tam>m:
            tam=tam-int(m)
            tam.save()
        else:
            messages.info(request,'not enough money with NGO')
            redirect('viewexpenditure')
        if money>0:
            texp=expenditure.objects.get(pk=1)
            texp.exp=texp.exp+int(m)
            texp.save()
        else:
            texp=expenditure(exp=int(m))
            texp.save()
        t=exphist(expe=int(m),rec=r)
        t.save()
        return redirect('viewexpenditure')
    return render(request,'update_expenditure.html')

def exph(request):
    m=expenditure.objects.all().count()
    if m>0:
        expend=exphist.objects.all()
        money=expenditure.objects.get(pk=1)
        return render(request,'expenditurehist.html',{'hist':expend,'total':money})
    else:
        return render(request,'update_expenditure.html')
        
    
    
    




def studentdetails(request):
    students = student.objects.order_by('-score').values()
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
    