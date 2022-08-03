from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models

NUM_BOXES = 5
BOXES = range(1, NUM_BOXES + 1)
user_name = get_user_model()


class Card(models.Model):
    question = models.CharField(max_length=40)
    answer = models.CharField(max_length=100)
    box = models.IntegerField(
        choices=zip(BOXES, BOXES),
        default=BOXES[0],
    )
    date_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(user_name, on_delete=models.CASCADE)

    def move(self, solved):
        new_box = self.box + 1 if solved else BOXES[0]

        if new_box in BOXES:
            self.box = new_box
            self.save()

        return self

    def __str__(self):
        return self.question
