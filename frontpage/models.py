# --- coding: utf-8 ---

"""
All models for the "Front page" application.
"""
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, RegexValidator
from django.db import models
from django.utils import timezone


class Jumbotron(models.Model):
    """Contents for Jumbotron."""

    class Meta:
        verbose_name = "Hero content"
        ordering = ['starting_datetime']

    cover_image = models.ImageField(upload_to='cover')
    title_text = models.CharField(max_length=100)
    subtitle_text = models.CharField(max_length=100, blank=True)
    lede_text = models.TextField(blank=True)
    button_label = models.CharField(max_length=20, default='Learn more')
    jump_url = models.CharField(max_length=200, blank=True)

    starting_datetime = models.DateTimeField(default=timezone.now)

    def __str__(self):
        if self.subtitle_text:
            return ' - '.join([self.title_text, self.subtitle_text])
        else:
            return self.title_text


class Product(models.Model):
    """Articles that explanes this application."""

    class Meta:
        verbose_name = "Product article"
        ordering = ['article_order']

    article_order = models.PositiveSmallIntegerField(
        unique=True,
        validators=[MinValueValidator(1)],
        default=1)
    title_text = models.CharField(max_length=100)
    product_image = models.ImageField(upload_to='product', blank=True)
    header_text = models.CharField(max_length=100, blank=True)
    sentence = models.TextField()
    tag_id = models.CharField(
        max_length=20,
        validators=[RegexValidator(regex='^[a-z0-9\-_]+$')],
        blank=True)

    def __str__(self):
        if self.header_text:
            return ' - '.join([self.title_text, self.header_text])
        else:
            return self.title_text
