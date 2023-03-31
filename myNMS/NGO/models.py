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
    sclass=models.IntegerField(null=True)
    books=models.IntegerField(null=True)
    uniforms=models.IntegerField(null=True)
    
class estimations(models.Model):
    sclass=models.IntegerField(null=True)
    books=models.IntegerField(null=True)
    uniforms=models.IntegerField(null=True)

class totalmoney(models.Model):
    Sum=models.IntegerField("money",null=True)
    
    


class Donor(models.Model):
     user = models.OneToOneField(User,on_delete=models.CASCADE)
     address=models.TextField('addressname',null=True)
     phone=models.BigIntegerField("mobileno",null=True)
    
class pledge(models.Model):
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
    books=models.BooleanField(null=True,default=False)
    uniform=models.BooleanField(null=True, default=False)
    performance=models.FloatField(null=True)
    gender=models.CharField(max_length=7,null=True)