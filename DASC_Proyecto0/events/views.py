
# Django

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Test
from django.http import HttpResponse

@login_required
def list_events(request):
    return HttpResponse('Hello List Events')