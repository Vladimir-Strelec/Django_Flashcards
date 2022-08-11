from django import template

from Django_Flashcards.cards.models import BOXES, Card

register = template.Library()


def boxes_as_links(current_user):
    boxes = []
    for box_num in BOXES:
        card_count = Card.objects.filter(box=box_num, user_id=current_user).count()
        boxes.append({
            "number": box_num,
            "card_count": card_count,
        })
    return boxes

