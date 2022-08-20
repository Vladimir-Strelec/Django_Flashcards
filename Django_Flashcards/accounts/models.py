from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, User
from django.core.validators import MinLengthValidator
from django.db import models

from Django_Flashcards.accounts.manager import CardUserManager
from Django_Flashcards.validators.validators import validate_only_letters



class CustomUser(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=50, validators=(MinLengthValidator(2), validate_only_letters), unique=True)
    email = models.EmailField()
    data_joined = models.DateTimeField(auto_now_add=True, )
    data_edit = models.DateTimeField(auto_now=True, )

    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'name'
    objects = CardUserManager()
    a = 5
