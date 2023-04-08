from django import forms
from django.forms import ModelForm
from .models import student,pledge

#create a student form 
class studentform(ModelForm):
    class Meta:
        model=student
        fields="__all__"
        
        #widgets
class pledgeform(ModelForm):
    class Meta:
        model=pledge
        fields=('money','books','uniform','frequency')
        
        #widgets
        