from django.db import models

# Create your models here.
class Donor(models.Model):
    firstname=models.CharField( max_length=120,null=True)
    lastname=models.CharField(max_length=120,null=True)
    email_id=models.EmailField('emailid',null=True)
    address=models.TextField('addressname',null=True)
    phone=models.BigIntegerField("mobileno",null=True)
    
    