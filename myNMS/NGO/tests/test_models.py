from django.test import TestCase
from NGO.models import student

class TestModels(TestCase):

    def setUp(self):
        self.project1=student.objects.create(
            name='Project 1',
            familyincome=100000
        )
    def score_test(self):
        category=.objects.create(

        )

