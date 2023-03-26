from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('adminlogin',views.adminlogin,name='login_admin'),
    path('donorlogin',views.donorlogin,name='login_donor'),

    path('donorRegistration',views.donorRegistration,name='register_donor'),
    path('logout',views.logout,name='logout'),
    path('viewDonor',views.donorview,name='viewDonor'),#3
    path('addstudent',views.addstu,name='add_student'),#1

    # path('pledgehist',views.pledge,'pledgehist'),#2
    # path('deletestudent',views.delstu,name='deletestudent'),#2
    # path('editesttbl',views.editest,name='editesttbl'),#2
    # path('viewworking',views.vstats,name='viewworking'),#3
    # path('viewpref',views.pref,name='viewpref'),#3
    # path('maintaininv',views.minventory,name='maintaininv'),#2
    path('aple',views.aple,name='addpledge'),#1
]