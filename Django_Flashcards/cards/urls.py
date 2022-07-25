from django.urls import path
from Django_Flashcards.cards.views import CardListView, CardCreateView, CardUpdateView

urlpatterns = (
    path("", CardListView.as_view(), name="card list"),
    path("create/", CardCreateView.as_view(), name="card create"),
    path("update/<int:pk>/", CardUpdateView.as_view(), name="card update"),
)
