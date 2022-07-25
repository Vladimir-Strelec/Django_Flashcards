from django.forms import ModelForm

from Django_Flashcards.cards.models import Card


class CreateCardForm(ModelForm):
    class Meta:
        model = Card
        fields = ['question', 'answer', 'box']


class UpdateCardForm(ModelForm):
    class Meta:
        model = Card
        fields = ['question', 'answer']