from django.contrib import admin
#from NGO.models import student,pledge,inventory,actual_money,estimations
from NGO.models import student,Pledge,Donor
# Register your models here.
admin.site.register(student)
admin.site.register(Pledge)
admin.site.register(Donor)
#admin.site.register(inventory)
#admin.site.register(actual_money)


