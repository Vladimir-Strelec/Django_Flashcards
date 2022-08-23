from django.test import TestCase
from django.urls import reverse

from Django_Flashcards.accounts.models import CustomUser
from Django_Flashcards.accounts.views import UserLoginView, DeleteProfile


class TestProfileView(TestCase):
    def setUp(self) -> None:
        self.user = CustomUser.objects.create(name='Test', email='test@gmail.com')
        self.user.save()
        self.data = {
            'name': 'Test',
            'email': 'test@gmail.com',
            'password1': 'v1',
            'password2': 'v1'
        }

    def test_register_view(self):
        data = {
            'name': 'Testov',
            'email': 'test@gmail.com',
            'password1': 'v1',
            'password2': 'v1'
        }
        self.assertEqual(1, CustomUser.objects.all().count())
        url = reverse('register')
        data = self.client.post(url, data=data)
        self.assertEqual(data.status_code, 302)
        self.assertEqual(2, CustomUser.objects.all().count())


    def test_login_view(self):
        url = reverse('login')
        response = self.client.post(url, data=self.data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_login_method_success(self):
        current_obj = UserLoginView()
        result = current_obj.get_success_url()
        self.assertEqual(result, '/')

    def test_delete_profile_method_success(self):
        current_obj = DeleteProfile()
        result = current_obj.get_success_url()
        self.assertEqual(result, '/')
