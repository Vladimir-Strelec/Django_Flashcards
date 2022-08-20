from django.contrib.auth import forms as auth_forms, get_user_model
from django import forms

from Django_Flashcards.accounts.models import CustomUser

UserModel = get_user_model()


class RegisterUserForm(auth_forms.UserCreationForm):

    class Meta:
        model = UserModel
        fields = ('name', 'email')
        # fields = '__all__'



class EditProfileForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ('name', 'email')


class DeleteProfileForm(forms.ModelForm):
    def save(self, commit=True):
        user = super().save(commit)
        user.delete()
        return self.instance

    class Meta:
        model = UserModel
        fields = ()
