from django.test import TestCase

from Django_Flashcards.cards.forms import DeleteCardForm
from Django_Flashcards.cards.models import Card


class TestCardForm(TestCase):
    def test_delete_card_form(self):
        self.assertEqual(Card.objects.all().count(), 0)
        card = Card.objects.create(question='test', answer='test', box=1)
        obj = DeleteCardForm(self)
        obj.instance = card
        obj.save()
        self.assertEqual(Card.objects.all().count(), 0)
