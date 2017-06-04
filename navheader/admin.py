# --- coding: utf-8 ---

"""
Register Model classes and ModelAdmin classes to the Django admin application.
"""
from django.contrib import admin

from .models import HeaderItem


class HeaderItemAdmin(admin.ModelAdmin):
    """
    Customaization of HeaderItem
    """

    list_display = ('item_order', 'edge', 'title_text', 'link_url')
    list_display_links = ('title_text',)


admin.site.register(HeaderItem, HeaderItemAdmin)
