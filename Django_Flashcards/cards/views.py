from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from Django_Flashcards.cards.forms import CreateCardForm
from Django_Flashcards.cards.models import Card


class CardListView(ListView):
    model = Card
    queryset = Card.objects.all().order_by("box",)
    template_name = 'card_list.html'


class CardCreateView(CreateView):
    template_name = 'card-form.html'
    form_class = CreateCardForm
    success_url = reverse_lazy(urls='card_create')
