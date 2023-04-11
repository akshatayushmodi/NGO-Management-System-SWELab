
from django.test import TestCase,Client
from django.urls import reverse,resolve
from django.contrib.auth import get_user
from NGO.models import *
from NGO.urls import *
class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.home_url = reverse('home')
        self.login_admin_url = reverse('login_admin')
        Admin.objects.create(username="Admin",password="User@111")
        self.admin_user = User.objects.create_user(
            username="Admin",
            password="User@111",
            is_staff=True        
        )

        self.test_user = User.objects.create_user(
            username="username",
            password="password"
        
        )
        
        self.test_Donor = Donor.objects.create(user = self.test_user,address="",phone=0)
        self.test_Pledge = pledge.objects.create(money=3000,donor=self.test_Donor,status=True,books=3,uniform=4)
        self.est_tbl = [estimations.objects.create(sclass=i,books=7,uniforms=22) for i in range(1,6)]
        self.total_money = totalmoney.objects.create(Sum=1000000)
        self.inv_tbl = [inventory.objects.create(sclass=i,books=20,uniforms=30) for i in range(1,6)]
        self.std_tbl = [student.objects.create(sclass=i,familyincome=1000,moneyneeded=30000,performance=90) for i in range(1,10)]
        self.expenditure_table = [expenditure.objects.create(exp=10) for i in range(1,5)]
    def test_home_GET(self):
        response = self.client.get(self.home_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'home.html')

    def test_adminlogin_GET(self):
        response = self.client.get(self.login_admin_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'login_admin.html')
    
    def test_adminlogin_POST(self):
        response_correct = self.client.post(self.login_admin_url,{
            
            'username':'Admin',
            'password':'User@111'
        
        })
        
        self.assertEquals(response_correct.status_code,200)
        self.assertTemplateUsed(response_correct,'adminpage.html')
        response_incorrect = self.client.post(self.login_admin_url,{
        
        'username':'Admin',
        'password':'Admin@000'
        
        })

        self.assertEquals(response_incorrect.status_code,302)
       
    def test_donor_login_GET(self):
        response = self.client.get(reverse('login_donor'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'login_donor.html')
    
    def test_donor_login_POST(self):
        response = self.client.post(reverse('login_donor'),{
            
            'username':'username',
            'password':'password'
        
        })
        
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'donorpage.html')
    
    def test_donor_login_redirect(self):
        response = self.client.post(reverse('login_donor'),{
            
            'username':'username',
            'password':'incorrect_password'
        
        })
        
        self.assertEquals(response.status_code,302)
        
    
    def test_donor_registration_GET(self):
        response = self.client.get(reverse('register_donor'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'register_donor.html')
    
    def test_donor_registration_redirect(self):
        response1 = self.client.post(reverse('register_donor'),{
            
        'first_name' : 'first_name',
        'last_name' :'last_name',
        'email_id' :'email_id',
        'phone_number' : 'phone_number',
        'username' : 'username',
        'address' : 'address',
        'password1' : 'password',
        'password2' : 'password'
        
        })
        
        self.assertEquals(response1.status_code,302)
        
        response2 = self.client.post(reverse('register_donor'),{
            
        'first_name' : 'first_name',
        'last_name' :'last_name',
        'email_id' :'email_id',
        'phone_number' : 'phone_number',
        'username' : 'username',
        'address' : 'address',
        'password1' : 'password',
        'password2' : 'password_not_match'
        
        })
        
        self.assertEquals(response2.status_code,302)
        
        
    def test_logout(self):
        response = self.client.get(reverse('logout'))
        self.assertEquals(response.status_code, 302)
        
    def test_donorview(self):
        response = self.client.get(reverse('viewDonor'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'donorsview.html')
    def test_addstu_POST(self):
        self.client.login(username='Admin',password='User@111')
        response = self.client.post(reverse('add_student'),{
            
            'fullname':'fullname',
            'sclass':'8',
            'familyincome':'1000',
            'moneyneeded':'15000',
            'books':'True',
            'performance':'97',
            'gender':'Female'
            
        
        })
        
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'adminpage.html')
    
    def test_aple_POST(self):
        self.client.login(username="username",password="password")
        response = self.client.post(reverse('addpledge'),{'money':'5000','books':'6','uniform':'3','frequency':'Onetime'})
        self.assertEquals(response.status_code,302)
        
    def test_pledgeh_GET(self):
        self.client.login(username='Admin',password='User@111')
        response = self.client.get(reverse('pledgehist'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'Pledgehistory.html')
    def test_viewdonor(self):
        response = self.client.get(reverse('show-donor',args=[1]))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'donorview.html')
    def test_clickp(self):
        self.client.login(username='Admin',password='User@111')
        response = self.client.get(reverse('click-paid',args=[1]))
        self.assertEquals(response.status_code, 302)
       
    def test_editest(self):
        self.client.login(username='Admin',password='User@111')
        response = self.client.get(reverse('editesttbl'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'estimates.html')
    def test_uro(self):
        self.client.login(username='Admin',password='User@111')
        response = self.client.post(reverse('update-row',args=[1]),{'book':'11','uniform':'10'})
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'est.html')
    def test_vstats(self):
        self.client.login(username='Admin',password='User@111')
        response = self.client.get(reverse('viewworking'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'workingstats.html')
        
    def test_minventory(self):
        self.client.login(username='Admin',password='User@111')
        response = self.client.get(reverse('maintaininv'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'inventoryview.html')
    def test_inven(self):
        self.client.login(username='Admin',password='User@111')
        response = self.client.post(reverse('update-inv',args=[1]),{'book':'11','uniform':'10'})
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'inve.html')
    def test_updatetexp(self):
        self.client.login(username='Admin',password='User@111')
        response = self.client.post(reverse('aexpend'),{'money':'1000','reason':'transport'})
        self.assertEquals(response.status_code,302)
    def test_exph(self):
        self.client.login(username='Admin',password='User@111')
        response = self.client.get(reverse('vexp'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'expenditurehist.html')
    def test_studentdetails(self):
        response = self.client.get(reverse('studentdetails'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'studentlist.html')
    def test_deletestudent(self):
        response = self.client.get(reverse('delete_student',args=[1]))
        self.assertEquals(response.status_code, 302)
    def test_modifystudent(self):
        response1 = self.client.post(reverse('modify_student',args=[1]),{
        'fullname':'student',
        'sclass':'3',
        'familyincome':'3000',
        'moneyneeded':'10000',
        'books':'True',
        'uniform':'False',
        'performance':'99',
        'gender':'Female'})
        self.assertEquals(response1.status_code,302)
        
        
        response2 = self.client.get(reverse('modify_student',args=[1]))
        self.assertEquals(response2.status_code,200)
        self.assertTemplateUsed(response2,'modifystudent.html')
    














