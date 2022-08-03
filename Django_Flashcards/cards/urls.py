from django.urls import path
from Django_Flashcards.cards.views import CardListView, CardCreateView, CardUpdateView, BoxView, CardDeleteView

urlpatterns = (
    path("", CardListView.as_view(), name="card list"),
    path("create/", CardCreateView.as_view(), name="card create"),
    path("update/<int:pk>/", CardUpdateView.as_view(), name="card update"),
    path("delete/<int:pk>/", CardDeleteView.as_view(), name="card delete"),
    path("box/<int:pk>/", BoxView.as_view(), name="header boxes"),
)
