from django.contrib.auth import get_user_model
from django.forms import models

User = get_user_model()


class EditProfileForm(models.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')


class DeleteProfileForm(models.ModelForm):
    def save(self, commit=True):
        user = super().save(commit)
        user.delete()
        self.instance.delete()
        return self.instance

    class Meta:
        model = User
        fields = ('username',)
