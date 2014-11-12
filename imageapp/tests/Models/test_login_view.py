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

    def test_login_page_loading(self):
        #setup
        response = self.client.get('/login')

        #Test
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Login now")
        self.assertContains(response, "Register now")

    def test_login_page_loads_home_with_right_credentials(self):
        #setup
        self.user.save()
        response = self.client.post('/login',data={
            'email': self.user.email,
            'password': self.user.password})

        #Test
        self.assertEqual(response.status_code, 302)
        self.assertRegexpMatches(response.url, 'home')

    def test_login_page_stays_in_login_with_wrong_password(self):
        #setup
        self.user.save()
        response = self.client.post('/login',data={
            'email': self.user.email,
            'password': self.user.password + 'wrong'})

        #Test
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Login Error!')

    def test_login_page_stays_in_login_with_wrong_email(self):
        #setup
        self.user.save()
        response = self.client.post('/login',data={
            'email': self.user.email + 'wrong',
            'password': self.user.password})

        #Test
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Login Error!')

    def test_login_page_form_validation(self):
        #setup
        response = self.client.post('/login',data={
            'email': '123',
            'password': ''});

        #Test
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'This field is required',count=1)
        self.assertContains(response, 'Enter a valid email address', count=1)





