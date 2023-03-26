from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('adminlogin',views.adminlogin,name='login_admin'),
    path('donorlogin',views.donorlogin,name='login_donor'),
    path('donorRegistration',views.donorRegistration,name='register_donor'),
    path('logout',views.logout,name='logout'),
    # path('viewDonor',views.donorview,name='viewDonor'),
    # path('pledgehist',views.pledge,'pledgehist'),#2
    # path('addstudent',views.addstu,'addstudent'),#1
    # path('deletestudent',views.delstu,'deletestudent'),#2
    # path('editesttbl',views.editest,'editesttbl'),#2
    # path('viewworking',views.vstats,'viewworking'),#3
    # path('viewpref',views.pref,'viewpref'),#3
    # path('maintaininv',views.minventory,'maintaininv'),#1,#2
    # path('addpledge',views.aple,'addpledge'),#1
]