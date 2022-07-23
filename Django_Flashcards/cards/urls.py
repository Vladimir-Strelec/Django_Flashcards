from django.urls import path

from Django_Flashcards.cards.views import TemplateView

urlpatterns = (path("", TemplateView.as_view(template_name="base.html"), name="home"),)

