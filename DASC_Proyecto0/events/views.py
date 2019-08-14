""" Controller's module for events app """
# Django

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist

# Forms
from events.forms import EventForm

# Models

from .models import Event
from .models import Category
from .models import EventType

# Test


@login_required
def list_events(request):
    """ Get the event's list generated by loged user """
    events = Event.objects.filter(event_creator=request.user).order_by('-event_create_date')
    context = {
        'events': events
    }
    return render(request, 'events/myevents.html', context = context)


@login_required
def create_event(request):
    """ Allow to create new events """
    if request.method == 'POST':
        pass
        #categories = Category.objects.all()
        #event_types = EventType.objects.all()
        #context = {
        #    'categories': categories,
        #    'event_types': event_types
        #}
    else:
        form = EventForm()
    print(form)
    return render(request, 
        'events/create.html', 
        context = {'form': form}
    )


@login_required
def edit_event(request):
    """ Edit information for event """
    if request.method == 'POST':
        pass
        #categories = Category.objects.all()
        #event_types = EventType.objects.all()
        #context = {
        #    'categories': categories,
        #    'event_types': event_types
        #}
    else:
        try:
            event = Event.objects.get(pk = request.GET['event'], event_creator = request.user )
            data = {
                'event_name': event.event_name,
                'event_site': event.event_site,
                'event_address': event.event_address,
                'event_start_date': event.event_start_date,
                'event_end_date': event.event_end_date,
                'event_category': event.event_category,
                'event_type': event.event_type
            }
            form = EventForm(initial = data)
            error = None
        except ObjectDoesNotExist:
            form = None
            error = 'Evento no encontrado, por favor reintente'
        print(form)
    return render(request, 
        'events/edit.html', 
        context = {
            'form': form, 
            'error': error
        })


@login_required
def delete_event(request):
    """ Delete an event from database """
    if request.method == 'GET':
        try:
            event = Event.objects.get(pk = request.GET['event'], event_creator = request.user)
            error = None
        except ObjectDoesNotExist:
            event = None
            error = 'Evento no encontrado, por favor reintente'
            
        context = {
            'event': event,
            'error': error
        }
    else:
        try:
            event = Event.objects.get(pk = request.POST['pk'], event_creator = request.user)
            event.delete()
            return redirect('events:myevents')
        except:
            context = {
                'error': 'No fue posible eliminar el registro, por favor reintente'
            }
    return render(request, 'events/delete.html', context = context)