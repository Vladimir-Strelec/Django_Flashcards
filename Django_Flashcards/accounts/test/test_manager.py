from django.contrib.auth import get_user_model
from django.test import TestCase

from Django_Flashcards.accounts.manager import CardUserManager
from Django_Flashcards.accounts.models import CustomUser
User = get_user_model()


class TestManager(TestCase):


    def test_method_create_user(self):
        self.assertEqual(CustomUser.objects.all().count(), 0)
        current_object = CardUserManager()
        current_object.model = User
        user = current_object.create_user(email='test@mail.ru', password='v1')
        self.assertEqual(user.email, 'test@mail.ru')
        self.assertEqual(CustomUser.objects.all().count(), 1)


    def test_method_create_superuser(self):
        self.assertEqual(CustomUser.objects.all().count(), 0)
        current_object = CardUserManager()
        current_object.model = User
        user = current_object.create_superuser(email='test@mail.ru', password='v1')
        self.assertEqual(user.email, 'test@mail.ru')
        self.assertEqual(CustomUser.objects.all().count(), 1)


    def test_method_create_superuser_with_not_is_staff(self):
        self.assertEqual(CustomUser.objects.all().count(), 0)
        current_object = CardUserManager()
        current_object.model = User
        with self.assertRaises(ValueError) as ex:
            current_object.create_superuser(email='test@mail.ru', password='v1', **{'is_staff': False})
        self.assertEqual(str(ex.exception), "Superuser must have is_staff=True.")
        self.assertEqual(CustomUser.objects.all().count(), 0)


    def test_method_create_superuser_with_not_is_superuser(self):
        self.assertEqual(CustomUser.objects.all().count(), 0)
        current_object = CardUserManager()
        current_object.model = User
        with self.assertRaises(ValueError) as ex:
            current_object.create_superuser(email='test@mail.ru', password='v1', **{'is_superuser': False})
        self.assertEqual(str(ex.exception), "Superuser must have is_superuser=True.")
        self.assertEqual(CustomUser.objects.all().count(), 0)
