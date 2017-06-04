# --- coding: utf-8 ---

"""
All models for the navigation header application.
"""
from django.core.validators import MinValueValidator
from django.db import models


class HeaderItem(models.Model):
    """Represent a item that has title text and link url."""

    class Meta:
        ordering = ['item_order']

    EDGE_CHOICE = (
        ('left', 'left'),
        ('right', 'right'),
    )

    item_order = models.PositiveSmallIntegerField(
        unique=True,
        validators=[MinValueValidator(1)],
        default=1)
    title_text = models.CharField(max_length=100)
    link_url = models.URLField()
    edge = models.CharField(max_length=10, choices=EDGE_CHOICE)

    def __str__(self):
        return self.title_text
