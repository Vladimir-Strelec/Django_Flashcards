from django.forms import ModelForm
from django import forms

from Django_Flashcards.cards.models import Card


class CreateCardForm(ModelForm):
    # user = forms.IntegerField()
    class Meta:
        model = Card
        fields = ['question', 'answer', 'box']




class UpdateCardForm(ModelForm):
    class Meta:
        model = Card
        fields = ['question', 'answer']


class DeleteCardForm(ModelForm):

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Card
        fields = ()


class CardCheckForm(forms.Form):
    card_id = forms.IntegerField(required=True)
    solved = forms.BooleanField(required=False)