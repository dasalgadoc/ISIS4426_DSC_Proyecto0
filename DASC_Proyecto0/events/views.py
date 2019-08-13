
# Django

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Test
from django.http import HttpResponse

@login_required
def list_events(request):
    return render(request, 'events/myevents.html')


@login_required
def create_event(request):
    return render(request, 'events/create.html')


@login_required
def edit_event(request):
    return render(request, 'events/edit.html')


@login_required
def delete_event(request):
    return render(request, 'events/delete.html')