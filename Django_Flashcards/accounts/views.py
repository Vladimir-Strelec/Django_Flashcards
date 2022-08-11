from django.contrib.auth import get_user_model
from django.contrib.auth import views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

from Django_Flashcards.accounts.forms import EditProfileForm, DeleteProfileForm, RegisterUserForm

User = get_user_model()


class RegisterView(generic.CreateView):
    form_class = RegisterUserForm
    template_name = 'register_account.html'
    success_url = reverse_lazy('login')


class UserLoginView(views.LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('card list')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


class UserLogout(views.LogoutView):
    template_name = 'login.html'


class ProfileView(LoginRequiredMixin, generic.DetailView):
    queryset = User.objects.all()
    template_name = 'profile.html'


class EditProfile(LoginRequiredMixin, generic.UpdateView):
    queryset = User.objects.all()
    form_class = EditProfileForm
    template_name = 'edit-profile.html'
    success_url = reverse_lazy('profile')


class ChangePassword(LoginRequiredMixin, views.PasswordChangeView):
    template_name = 'change-password.html'
    success_url = reverse_lazy('login')


class DeleteProfile(LoginRequiredMixin, generic.UpdateView):
    queryset = User.objects.all()
    form_class = DeleteProfileForm
    success_url = reverse_lazy('card list')
    template_name = 'delete-profile.html'

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()

