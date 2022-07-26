from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView

from Django_Flashcards.cards.forms import CreateCardForm, UpdateCardForm
from Django_Flashcards.cards.models import Card


class CardListView(ListView):
    model = Card
    queryset = Card.objects.all().order_by("box",)
    template_name = 'card_list.html'


class BoxView(CardListView):
    template_name = "box.html"

    def get_queryset(self):
        return Card.objects.filter(box=self.kwargs["pk"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["box_number"] = self.kwargs["pk"]
        return context


class CardCreateView(CreateView):
    template_name = 'card-create-update.html'
    form_class = CreateCardForm
    success_url = reverse_lazy('card create')


class CardUpdateView(CardCreateView, UpdateView):
    form_class = UpdateCardForm
    queryset = Card.objects.all()
    template_name = 'card-create-update.html'
    success_url = reverse_lazy("card list")

