""" User's forms """

# Django

from django import forms

# Models

from django.contrib.auth.models import User
from users.models import PasswordRetrieval


class SignupForm(forms.Form):
    """ Custom form to sign up new users """

    username = forms.CharField(min_length = 5, max_length = 140, required = True)
    password = forms.CharField(max_length = 35, required = True)
    password_confirmation = forms.CharField(max_length = 35, required = True)

    secret_question = forms.CharField(max_length = 140, required = False)
    secret_answer = forms.CharField(max_length = 100, required = False)
    
    def clean_username(self):
        """ Method to validate if user exists """
        username = self.cleaned_data['username']
        username_taken = User.objects.filter(username=username).exists()

        if username_taken:
            raise forms.ValidationError('Este usuario ya se encuentra registrado.')

        return username

    def clean(self):
        """ Verify password confirmation match. """

        data = super().clean()

        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError('Las contraseñas no coinciden.')

        return data

    def save(self):
        """ Create a new user """

        data = self.cleaned_data
        data.pop('password_confirmation')

        user = User.objects.create_user(**data)
        password_retrieval = PasswordRetrieval(user = user)

        password_retrieval.save()

