# --- coding: utf-8 ---

"""
frontpage URL Configuration
"""
from django.conf.urls import url
from django.contrib import admin

from .views import FrontView

urlpatterns = [
    url(r'^$', FrontView.as_view(), name='frontpage'),
]
