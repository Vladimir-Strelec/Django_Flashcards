import random

from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from Django_Flashcards.cards.forms import CreateCardForm, UpdateCardForm, CardCheckForm, DeleteCardForm
from Django_Flashcards.cards.models import Card
from template_tags.cards_tags import boxes_as_links

UserModel = get_user_model()


class CardListView(ListView):
    model = Card
    queryset = Card.objects.all().order_by("box",)
    template_name = 'card_list.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['boxes_count'] = boxes_as_links(self.request.user)
        context['current_card_user'] = Card.objects.filter(user_id=self.request.user.id).order_by('box',)
        return context

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)


class BoxView(CardListView):
    template_name = "box.html"
    form_class = CardCheckForm

    def get_queryset(self):
        return Card.objects.filter(box=self.kwargs["pk"], user_id=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['boxes_count'] = boxes_as_links(self.request.user)
        context['box_number'] = self.kwargs['pk']
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


    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)


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


