import random

from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from Django_Flashcards.cards.forms import CreateCardForm, UpdateCardForm, CardCheckForm, DeleteCardForm
from Django_Flashcards.cards.models import Card
from template_tags.cards_tags import boxes_as_links

user_name = get_user_model()


class CardListView(ListView):
    model = Card
    queryset = Card.objects.all().order_by("box", )
    template_name = 'card_list.html'

    # def get_queryset(self):
    #     return Card.objects.filter(box=self.kwargs["pk"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['boxes_count'] = boxes_as_links()
        return context


class BoxView(CardListView):
    template_name = "box.html"
    form_class = CardCheckForm

    def get_queryset(self):
        return Card.objects.filter(box=self.kwargs["pk"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['boxes_count'] = boxes_as_links()
        context["box_number"] = self.kwargs["pk"]
        if self.object_list:
            context["check_card"] = random.choice(self.object_list)
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            card = get_object_or_404(Card, id=form.cleaned_data['card_id'])
            card.move(form.cleaned_data['solved'])
        return redirect(request.META.get("HTTP_REFERER"))


class CardCreateView(CreateView):
    template_name = 'card-create-update.html'
    form_class = CreateCardForm
    success_url = reverse_lazy('card create')
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        form.cleaned_data['user'] = request.user
        if form.is_valid():
            form.save()


class CardUpdateView(CardCreateView, UpdateView):
    form_class = UpdateCardForm
    template_name = 'card-create-update.html'
    success_url = reverse_lazy("card list")


class CardDeleteView(DeleteView):
    model = Card
    form_class = DeleteCardForm
    queryset = Card.objects.all()
    template_name = 'card-delete-update.html'
    success_url = reverse_lazy("card list")

    # def get(self, request, *args, **kwargs):
    #     obj = Card.objects.get(id=kwargs['pk'])
    #     obj.delete()
    #     return obj
