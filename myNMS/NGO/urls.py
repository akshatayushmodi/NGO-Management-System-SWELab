from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('adminlogin',views.adminlogin,name='login_admin'),
    path('donorlogin',views.donorlogin,name='login_donor'),
    path('donorRegistration',views.donorRegistration,name='register_donor'),
    path('logout',views.logout,name='logout'),
    path('viewDonor',views.donorview,name='viewDonor'),#3
    path('aple',views.aple,name='addpledge'),#1
    path('addstudent',views.addstu,name='add_student'),
    path('viewDonor',views.donorview,name='viewDonor'),
    path('pledgehist',views.pledgeh,'pledgehist'),
    path('deletestudent',views.delstu,name='deletestudent'),
    path('editesttbl',views.editest,name='editesttbl'),
    path('viewworking',views.vstats,name='viewworking'),
    path('viewpref',views.pref,name='viewpref'),
    path('maintaininv',views.minventory,name='maintaininv'),
]
    

