from django import template

from Django_Flashcards.cards.models import BOXES, Card

register = template.Library()


def boxes_as_links():
    boxes = []
    for box_num in BOXES:
        card_count = Card.objects.filter(box=box_num).count()
        boxes.append({
            "number": box_num,
            "card_count": card_count,
        })
    return boxes

