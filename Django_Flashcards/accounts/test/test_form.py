from unittest import TestCase
from Django_Flashcards.wsgi import *
from Django_Flashcards.accounts.forms import DeleteProfileForm, RegisterUserForm
from Django_Flashcards.accounts.models import CustomUser


class PermissionAPITestcase(TestCase):
    def test_create_custom_user(self):
        self.data = {
            'name': 'test',
            'email': 'test1@gmail.com',
            'password1': 'v1',
            'password2': 'v1',


        }
        form = RegisterUserForm(data=self.data)


        self.assertTrue(form.is_valid())


