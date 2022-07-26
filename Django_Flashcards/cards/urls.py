from django.urls import path
from Django_Flashcards.cards.views import CardListView, CardCreateView, CardUpdateView, BoxView

urlpatterns = (
    path("", CardListView.as_view(), name="card list"),
    path("create/", CardCreateView.as_view(), name="card create"),
    path("update/<int:pk>/", CardUpdateView.as_view(), name="card update"),
    path("box/<int:pk>/", BoxView.as_view(), name="card update"),
)
