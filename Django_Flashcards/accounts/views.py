from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView

from django.urls import reverse_lazy
from django.views import generic

from Django_Flashcards.accounts.forms import EditProfileForm, DeleteProfileForm

User = get_user_model()


class RegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'register_account.html'
    success_url = reverse_lazy('login')


class UserLoginView(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('card list')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


class ProfileView(generic.DetailView):
    queryset = User.objects.all()
    template_name = 'profile.html'


class EditProfile(generic.UpdateView):
    queryset = User.objects.all()
    form_class = EditProfileForm
    template_name = 'edit-profile.html'
    success_url = reverse_lazy('profile')


class DeleteProfile(generic.UpdateView):
    queryset = User.objects.all()
    form_class = DeleteProfileForm
    success_url = reverse_lazy('card list')
