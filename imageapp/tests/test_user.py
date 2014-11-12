from django.test import TestCase

from imageapp.models import User

class QuestionMethodTests(TestCase):

    def create_test_user(self):
        first_name = "Joe"
        second_name = "Man"
        email = "joe@asu.edu"
        password = "password"

        return  User(first_name=first_name, second_name=second_name, email=email, password=password)

    def test_user_gives_full_name(self):
        #setup
        user = self.create_test_user()

        #Call
        full_name = user.full_name()

        #Test
        self.assertEqual(full_name, "Joe Man")

    def test_hashing_password_check_is_right(self):
        #setup
        user = self.create_test_user()
        hash = user.hash_password('password')

        result = user.check_password('password', hash)

        self.assertTrue(result)

    def test_returns_valid_user_if_exists(self):
        #setup
        user = self.create_test_user()
        user.save()

        #Call
        new_user = user.return_valid_user("joe@asu.edu", "password")

        #Test
        self.assertEqual(new_user, user)

    def test_returns_none_on_valid_user_if_wrong_password(self):
        #setup
        user = self.create_test_user()
        user.save()

        #Call
        new_user = user.return_valid_user("joe@asu.edu", "wrong-password")

        #Test
        self.assertNotEqual(new_user, user)

    def test_returns_none_on_valid_user_if_wrong_email(self):
        #setup
        user = self.create_test_user()
        user.save()

        #Call
        new_user = user.return_valid_user("wrong@email.edu", "password")

        #Test
        self.assertNotEqual(new_user, user)

