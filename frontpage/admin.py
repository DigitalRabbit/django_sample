# --- coding: utf-8 ---

"""
Register Model classes and ModelAdmin classes to the Django admin application.
"""
from django.contrib import admin
from .models import Jumbotron, Product


class JumbotronAdmin(admin.ModelAdmin):
    """
    Customaization of Jumbotron
    """

    list_display = ('__str__', 'starting_datetime')


class ProductAdmin(admin.ModelAdmin):
    """
    Customaization of Product
    """

    list_display = ('article_order', '__str__')
    list_display_links = ('__str__',)


admin.site.register(Jumbotron, JumbotronAdmin)
admin.site.register(Product, ProductAdmin)
