from django.db import models
from django.contrib.auth.models import User

# from django_postgres_extensions.models.fields import ArrayField


# Create your models here.
# class Donor(models.Model):
#     firstname=models.CharField( max_length=120,null=True)
#     lastname=models.CharField(max_length=120,null=True)
#     email_id=models.EmailField('emailid',null=True)
#     address=models.TextField('addressname',null=True)
#     phone=models.BigIntegerField("mobileno",null=True)
class inventory(models.Model):
    sclass=models.PositiveIntegerField(null=True)
    books=models.PositiveIntegerField(null=True)
    uniforms=models.PositiveIntegerField(null=True)

class Admin(models.Model):
    username=models.CharField(max_length=120,null=True)
    password=models.CharField(max_length=120,null=True)
class estimations(models.Model):
    sclass=models.PositiveIntegerField(null=True)
    books=models.PositiveIntegerField(null=True)
    uniforms=models.PositiveIntegerField(null=True)

class totalmoney(models.Model):
    Sum=models.PositiveIntegerField("money",null=True)
    
class expenditure(models.Model):
    exp=models.PositiveIntegerField(null=True)
    
class exphist(models.Model):
    expe=models.PositiveIntegerField(null=True)
    rec=models.CharField(max_length=801,null=True)


class Donor(models.Model):
     user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
     address=models.TextField('addressname',null=True)
     phone=models.BigIntegerField("mobileno",null=True)
    
class pledge(models.Model):
    money=models.PositiveBigIntegerField("paisa",null=True)
    donor=models.ForeignKey(Donor,null=True,on_delete=models.CASCADE)
    status=models.BooleanField(null=True)
    ubstatus=models.BooleanField(null=True)
    time=models.DateTimeField(null=True)
    lastpaid=models.DateTimeField(null=True)
    #frequency
    frequency=models.CharField(max_length=120,null=True)
    books=models.PositiveSmallIntegerField(null=True)
    uniform=models.PositiveSmallIntegerField(null=True)#stores class

class student(models.Model):
    fullname=models.CharField(max_length=240,null=True)
    sclass=models.PositiveSmallIntegerField(null=True)
    familyincome=models.PositiveIntegerField(null=True)
    moneyneeded=models.PositiveIntegerField(null=True)
    books=models.BooleanField(null=True,default=False)
    uniform=models.BooleanField(null=True, default=False)
    performance=models.FloatField(null=True)
    gender=models.CharField(max_length=7,null=True)
    score=models.FloatField(null=True)

    def __score__(self):
        income_coeff=0.5
        income_limit=500000.0
        gender_flag = 0
        performance_coeff=0.37
        gender_coefficient=1-income_coeff-performance_coeff
        if(self.gender=="Female"):
            gender_flag=1
        
        new_score = income_coeff*(income_limit-int(self.familyincome))/income_limit+performance_coeff*float(self.performance)/100+gender_coefficient*gender_flag/2
        self.score = float(new_score)
    
