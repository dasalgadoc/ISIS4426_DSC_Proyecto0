from django.shortcuts import render

# Test
from django.http import HttpResponse

def list_events(request):
    return HttpResponse('Hello List Events')