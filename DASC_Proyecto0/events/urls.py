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
    path(
        route='create/',
        view=views.create_event,
        name='create'
    ),
    path(
        route='edit/',
        view=views.edit_event,
        name='edit'
    ),
    path(
        route='delete/',
        view=views.delete_event,
        name='delete'
    ),
    
]