from django.contrib.auth import get_user_model
from django.contrib.auth import forms
from django.forms import models

from Django_Flashcards.accounts.models import CustomUser

UserModel = get_user_model()


class RegisterUserForm(forms.UserCreationForm):

    class Meta:
        model = UserModel
        fields = ('name', 'email')
        # fields = '__all__'



class EditProfileForm(models.ModelForm):
    class Meta:
        model = UserModel
        fields = ('name', 'email')


class DeleteProfileForm(models.ModelForm):
    def save(self, commit=True):
        user = super().save(commit)
        user.delete()
        self.instance.delete()
        return self.instance

    class Meta:
        model = UserModel
        fields = ()
