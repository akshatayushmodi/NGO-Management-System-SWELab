from django.contrib import admin
#from NGO.models import student,pledge,inventory,actual_money,estimations

from NGO.models import student,pledge,totalmoney,inventory,estimations,Donor,exphist,expenditure,Admin
# Register your models here.
admin.site.register(student)
admin.site.register(pledge)
admin.site.register(totalmoney)
admin.site.register(inventory)
admin.site.register(estimations)

admin.site.register(Donor)
admin.site.register(expenditure)
admin.site.register(exphist)
admin.site.register(Admin)


