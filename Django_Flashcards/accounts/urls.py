from django.urls import path

from Django_Flashcards.accounts.views import RegisterView, UserLoginView, ProfileView, EditProfile, DeleteProfile, \
    UserLogout, ChangePassword

urlpatterns = (
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/<int:pk>/', UserLogout.as_view(), name='logout'),


    path('accounts/profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('edit/profile/<int:pk>/', EditProfile.as_view(), name='edit profile'),
    path('change/pasword/<int:pk>/', ChangePassword.as_view(), name='change password'),
    path('delete/profile/<int:pk>/', DeleteProfile.as_view(), name='delete profile'),

)
