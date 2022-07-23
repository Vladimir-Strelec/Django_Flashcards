from django.shortcuts import render
from django.views.generic import TemplateView


class TemplateView(TemplateView):
    template_name = 'base.html'
