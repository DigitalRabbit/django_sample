# --- coding: utf-8 ---

"""
All views for the frontpage application.
"""
from django.conf import settings
from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Jumbotron, Product


class FrontView(TemplateView):
    """A view class that represents a front page of site."""

    template_name = 'frontpage/index.html'

    def get_context_data(self, **kwargs):
        context = super(FrontView, self).get_context_data(**kwargs)
        context['jumbotron'] = Jumbotron.objects.get(pk=1)
        context['product_list'] = Product.objects.all()
        return context
