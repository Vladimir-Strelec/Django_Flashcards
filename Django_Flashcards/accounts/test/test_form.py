import json

from django.test.client import Client
from django.test import TestCase
from django.urls import reverse

from Django_Flashcards.wsgi import *
from Django_Flashcards.accounts.forms import RegisterUserForm, EditProfileForm
from Django_Flashcards.accounts.models import CustomUser


class PermissionAPITestcase(TestCase):
    def setUp(self) -> None:
        self.data = {
            'name': 'Test',
            'email': 'test1@gmail.com',
            'password1': 'v1',
            'password2': 'v1',
        }
        self.user = CustomUser.objects.create(name='ova', email='vova@gmail.com', password='v1')

    def test_create_custom_user_form_is_valid(self):
        form = RegisterUserForm(data=self.data)
        self.assertTrue(form.is_valid())

    def test_create_custom_user_form_not_valid(self):
        custom_data = {
            'name': 'test',
        }
        form = RegisterUserForm(data=custom_data)
        self.assertFalse(form.is_valid())

    def test_edit_profile_form(self):
        form = EditProfileForm(data=self.data)
        self.assertTrue(form.is_valid())
