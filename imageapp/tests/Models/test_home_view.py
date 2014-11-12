from django.test import TestCase
from django.test.utils import setup_test_environment
from django.test import Client
from imageapp.tests.Models import test_helper

from imageapp.models import User
from imageapp.models import Picture
import imageapp.views

class QuestionMethodTests(TestCase):

    def setUp(self):
        first_name = "Joe"
        second_name = "Man"
        email = "joe@asu.edu"
        password = "password"

        self.user = User(first_name=first_name, second_name=second_name, email=email, password=password)
        self.user.save()
        Picture(user=self.user, photo='First_photo.png').save()
        Picture(user=self.user, photo='Second_photo.png').save()

        self.client = Client()
        self.client.post('/login',data={
            'email': self.user.email,
            'password': self.user.password})


    def test_home_page(self):
        #setup
        response = self.client.get('/home')

        #Test
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Logout')
        self.assertContains(response, 'Setting')

    def test_home_page_without_login_redirects_to_login(self):
        #setup
        self.client.get('/logout')
        response = self.client.get('/home')

        #Test
        self.assertEqual(response.status_code, 302)
        self.assertRegexpMatches(response.url, 'login')

    def test_home_page_sends_pictures(self):
        #setup
        response = self.client.get('/home')

        #Test
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.user.pictures.all()[0].photo.name)
        self.assertContains(response, self.user.pictures.all()[1].photo.name)
