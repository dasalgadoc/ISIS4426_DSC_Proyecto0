""" Event's admin module """

# Django

from django.contrib import admin

# Models

from .models import EventType, Category, Event

# Model Registry

admin.site.register(EventType)
admin.site.register(Category)
admin.site.register(Event)
