from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("Django_Flashcards.cards.urls")),
    path("", include("Django_Flashcards.accounts.urls")),

]
