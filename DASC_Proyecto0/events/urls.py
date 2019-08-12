""" App's Events URL """

# Django
from django.urls import path

# Views
from events import views

urlpatterns = [
    path(
        route='',
        view = views.list_events,
        name='myevents'
    ),
]