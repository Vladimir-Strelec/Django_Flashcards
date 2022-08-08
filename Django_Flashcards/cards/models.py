from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.db import models

NUM_BOXES = 5
BOXES = range(1, NUM_BOXES + 1)
user_name = get_user_model()


class Card(models.Model):
    MIN_LENGTH = 2
    MAX_LENGTH = 100
    question = models.CharField(max_length=MAX_LENGTH, validators=(MinLengthValidator(MIN_LENGTH),))
    answer = models.CharField(max_length=MAX_LENGTH, validators=(MinLengthValidator(MIN_LENGTH),))
    box = models.IntegerField(
        choices=zip(BOXES, BOXES),
        default=BOXES[0],
    )
    date_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(user_name, on_delete=models.CASCADE, blank=True, null=True)

    def move(self, solved):
        new_box = self.box + 1 if solved else BOXES[0]

        if new_box in BOXES:
            self.box = new_box
            self.save()

        return self

    def __str__(self):
        return self.question
