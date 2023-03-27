from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class Donor(models.Model):
#     firstname=models.CharField( max_length=120,null=True)
#     lastname=models.CharField(max_length=120,null=True)
#     email_id=models.EmailField('emailid',null=True)
#     address=models.TextField('addressname',null=True)
#     phone=models.BigIntegerField("mobileno",null=True)

class pledge(models.Model):
    money=models.IntegerField("Money",null=True)
    #frequency
    books=models.IntegerField(null=True)
    uniform=models.IntegerField(null=True)#stores class
    donor=models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    status=models.BooleanField(null=True)

class student(models.Model):
    fullname=models.CharField(max_length=240,null=True)
    sclass=models.SmallIntegerField(null=True)
    familyincome=models.IntegerField(null=True)
    moneyneeded=models.IntegerField(null=True)
    books=models.BooleanField(null=True)
    uniform=models.BooleanField(null=True)
    performance=models.FloatField(null=True)
    gender=models.CharField(max_length=7,null=True)