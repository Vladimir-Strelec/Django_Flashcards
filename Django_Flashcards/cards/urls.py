from django.urls import path

from Django_Flashcards.cards import views
from Django_Flashcards.cards.views import CardListView, CardCreateView

urlpatterns = (
    path("", CardListView.as_view(), name="card_list"),
    path("new/", views.CardCreateView.as_view(), name="card_create"),
)
