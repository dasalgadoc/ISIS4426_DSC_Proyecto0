
# Django

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Forms

from users.forms import SignupForm, ForgotPasswordForm

# Models

from django.contrib.auth.models import User

# Test
from django.http import HttpResponse

# View's methods start

def login_view(request):
    """ Login Method """
    if(request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('events:myevents')
        else:
            return render(request, 'users/login.html', {'error': 'Nombre de usuario o contraseña no valido'})
    
    return render(request, 'users/login.html')


@login_required
def logout_view(request):
    """ Logout Method """
    logout(request)
    return redirect('login')


def signup(request):
    """ Sign up controllers method to create new users """
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()

    return render(
        request=request,
        template_name='users/signup.html',
        context={'form': form}
    )


def forgot_password(request):
    """ Controllers that handles with password forget users """
    
    if request.method == 'POST':
        form = ForgotPasswordForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            
            user = data['username']
            print(User.objects.get(username=user).password)

            
    else:
        form = ForgotPasswordForm()
    
    return render(
        request = request,
        template_name= 'users/retrieval.html',
        context={
            'form': form
        }
    )