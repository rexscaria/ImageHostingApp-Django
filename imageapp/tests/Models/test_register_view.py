from django.test import TestCase
from django.test.utils import setup_test_environment
from django.test import Client
from imageapp.tests.Models import test_helper

from imageapp.models import User
import imageapp.views

class QuestionMethodTests(TestCase):

    def setUp(self):
        first_name = "Joe"
        second_name = "Man"
        email = "joe@asu.edu"
        password = "password"

        self.user = User(first_name=first_name, second_name=second_name, email=email, password=password)

        self.client = Client()

    def test_registration_page(self):
        #setup
        response = self.client.post('/register',data={
            'first_name': self.user.first_name,
            'second_name': self.user.second_name,
            'email': self.user.email,
            'password': self.user.password});

        test_user = User.return_valid_user(self.user.email, self.user.password)


        #Test
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Registration success')
        self.assertTrue(test_helper.obj_compare(self.user, test_user,['id','_state']))

    def test_registration_page_form_validation(self):
        #setup
        response = self.client.post('/register',data={
            'first_name': '',
            'second_name': '',
            'email': '123',
            'password': ''});

        #Test
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'This field is required',count=3)
        self.assertContains(response, 'Enter a valid email address', count=1)

    def test_dont_register_existing_email_idn(self):
        #setup
        self.user.save()
        response = self.client.post('/register',data={
            'first_name': self.user.first_name,
            'second_name': self.user.second_name,
            'email': self.user.email,
            'password': self.user.password});

        #Test
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'User with this Email already exists',count=1)

