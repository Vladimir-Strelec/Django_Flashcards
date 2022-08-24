from django.test import TestCase
from django.urls import reverse

from Django_Flashcards.accounts.models import CustomUser
from Django_Flashcards.cards.forms import CardCheckForm
from Django_Flashcards.cards.models import Card


class TestCardsView(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(name='Vova', email='test@mail.ru')
        self.card = Card.objects.create(question='test', answer='test', box=1, user=self.user)
        self.data = {
            'question': 'test',
            'answer': 'test',
            'box': 1,
        }

    def test_card_list_view_wth_here_methods(self):
        url = reverse('card list')

        self.client.force_login(self.user)
        response = self.client.get(url, data=self.data)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'card.html')

        self.assertEqual(len(response.context_data['boxes_count']), 5)
        self.assertEqual(response.context_data['current_card_user'][0].user.name, 'Vova')


    def test_card_list_view_method_dispatch(self):
        url = reverse('card list')
        response = self.client.get(url, data=self.data)
        result = self.client.get(response.url, data=self.data)
        self.assertTemplateUsed(result, 'login.html')


    def test_box_view_and_context_data(self):
        self.client.force_login(self.user)
        url = reverse('header boxes', args=(self.card.box,))
        response = self.client.get(url, data=self.data)

        self.assertEqual(len(response.context_data['boxes_count']), 5)
        self.assertEqual(response.context_data['box_number'], self.card.box)
        self.assertEqual(response.context_data['check_card'], self.card)



