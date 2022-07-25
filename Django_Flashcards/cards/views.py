from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView

from Django_Flashcards.cards.forms import CreateCardForm, UpdateCardForm
from Django_Flashcards.cards.models import Card


class CardListView(ListView):
    model = Card
    queryset = Card.objects.all().order_by("box",)
    template_name = 'card_list.html'


class CardCreateView(CreateView):
    template_name = 'card-create.html'
    form_class = CreateCardForm
    success_url = reverse_lazy('card create')


class CardUpdateView(CardCreateView, UpdateView):
    form_class = UpdateCardForm
    queryset = Card.objects.all()
    template_name = 'card-update.html'
    success_url = reverse_lazy("card list")

