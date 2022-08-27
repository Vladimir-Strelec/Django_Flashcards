from django.contrib import admin

from Django_Flashcards.cards.models import Card


@admin.register(Card)
class CardModelAdmin(admin.ModelAdmin):
    pass
