from django.test import TestCase
from django.urls import reverse,resolve
from NGO.views import *
class TestUrls(TestCase):

    def test_home_url_is_resolved(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func,home)
    
    def test_admin_login_url_is_resolved(self):
        url = reverse('login_admin')
        self.assertEquals(resolve(url).func,adminlogin)
    
    def test_donor_login_url_is_resolved(self):
        url = reverse('login_donor')
        self.assertEquals(resolve(url).func,donorlogin)

    def test_register_donor_login_url_is_resolved(self):
        url = reverse('register_donor')
        self.assertEquals(resolve(url).func,donorRegistration)
    
    def test_logout_url_is_resolved(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func,logout)
    
    def test_viewDonor_url_is_resolved(self):
        url = reverse('viewDonor')
        self.assertEquals(resolve(url).func,donorview)
    
    def test_pledgehist_url_is_resolved(self):
        url = reverse('pledgehist')
        self.assertEquals(resolve(url).func,pledgeh)
    
    def test_studentdetails_url_is_resolved(self):
        url = reverse('studentdetails')
        self.assertEquals(resolve(url).func,studentdetails)
    
    def test_delete_student_url_is_resolved(self):
        url = reverse('delete_student',args=[0])
        self.assertEquals(resolve(url).func,deletestudent)
    
    def test_modify_student_url_is_resolved(self):
        url = reverse('modify_student',args=[0])
        self.assertEquals(resolve(url).func,modifystudent)
    
    def test_edit_estimation_table_url_is_resolved(self):
        url = reverse('editesttbl')
        self.assertEquals(resolve(url).func,editest)
    
    def test_working_status_url_is_resolved(self):
        url = reverse('viewworking')
        self.assertEquals(resolve(url).func,vstats)
    
    def test_maintain_inventory_url_is_resolved(self):
        url = reverse('maintaininv')
        self.assertEquals(resolve(url).func,minventory)
    
    def test_show_donor_url_is_resolved(self):
        url = reverse('show-donor',args=[0])
        self.assertEquals(resolve(url).func,viewdonor)
    
    def test_click_paid_url_is_resolved(self):
        url = reverse('click-paid',args=[0])
        self.assertEquals(resolve(url).func,clickp)
    
    def test_update_row_url_is_resolved(self):
        url = reverse('update-row',args=[1])
        self.assertEquals(resolve(url).func,uro)
    
    def test_update_inv_url_is_resolved(self):
        url = reverse('update-inv',args=[1])
        self.assertEquals(resolve(url).func,inven)
    
    def test_exph_url_is_resolved(self):
        url = reverse('vexp')
        self.assertEquals(resolve(url).func,exph)
    
    def test_aexpend_url_is_resolved(self):
        url = reverse('aexpend')
        self.assertEquals(resolve(url).func,updatetexp)



































