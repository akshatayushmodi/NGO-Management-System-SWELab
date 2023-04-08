from django.test import TestCase
from NGO.models import student

class TestModels(TestCase):

    @classmethod
    def setUp(cls):
        student.objects.create(fullname='ishan',sclass=1,familyincome=100000,moneyneeded=50000,books=True,uniform=False,performance=80,gender='Male')

    def test_score(self):
        stu=student.objects.get(id=1)
        income_coeff=0.4
        income_limit=500000.0
        gender_flag = 0
        performance_coeff=0.3
        gender_coefficient=1-income_coeff-performance_coeff
        if(stu.gender=="Female"):
            gender_flag=1
        
        new_score = income_coeff*(income_limit-(stu.familyincome))/income_limit+performance_coeff*(stu.performance)/100+gender_coefficient*gender_flag/2
        exp_output=float(new_score)
        stu.__score__()
        self.assertEqual(exp_output,stu.score)