from django.db import models
from django.contrib.auth.models import User


class Donor(models.Model):
     user = models.OneToOneField(User,on_delete=models.CASCADE)
     address=models.TextField('addressname',null=True)
     phone=models.BigIntegerField("mobileno",null=True)
    
class Pledge(models.Model):
    money=models.PositiveBigIntegerField("paisa",null=True)
    donor=models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    status=models.BooleanField(null=True)
    #frequency
    books=models.PositiveSmallIntegerField(null=True)
    uniform=models.PositiveSmallIntegerField(null=True)#stores class

class student(models.Model):
    fullname=models.CharField(max_length=240,null=True)
    sclass=models.SmallIntegerField(null=True)
    familyincome=models.IntegerField(null=True)
    moneyneeded=models.IntegerField(null=True)
    books=models.BooleanField(null=True)
    uniform=models.BooleanField(null=True)
    performance=models.FloatField(null=True)
    gender=models.CharField(max_length=7,null=True)