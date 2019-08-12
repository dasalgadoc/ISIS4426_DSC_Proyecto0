from django.shortcuts import render

# Test
from django.http import HttpResponse

def login_view(request):
    return HttpResponse('Hello login view')


def logout_view(request):
    return HttpResponse('Hello logout')


def signup(request):
    return HttpResponse('Hello signups')


