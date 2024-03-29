""" User's forms """

# Django

from django import forms
from django.core.exceptions import ObjectDoesNotExist

# Models

from django.contrib.auth.models import User
from users.models import PasswordRetrieval

# Util
import re

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

        mail_validation = re.findall(".+@.+\..+",username)

        if not mail_validation:
            raise forms.ValidationError('El usuario debe ser un email valido')

        if username_taken:
            raise forms.ValidationError('Este usuario ya se encuentra registrado.')

        return username

    def clean(self):
        """ Verify password confirmation match. """

        data = super().clean()

        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError({'password': ["Las contraseñas no coinciden!",]})

        return data

    def save(self):
        """ Create a new user """

        data = self.cleaned_data
        secret_question = data['secret_question']
        secret_answer = data['secret_answer']

        data.pop('password_confirmation')
        data.pop('secret_question')
        data.pop('secret_answer')

        user = User.objects.create_user(**data)
        password_retrieval = PasswordRetrieval(user = user, 
            secret_answer = secret_answer, 
            secret_question = secret_question)

        password_retrieval.save()


class ForgotPasswordForm(forms.Form):
    """ Password retrieval form """
    username = forms.CharField(min_length = 5, max_length = 140, required = True)

    secret_question = forms.CharField(max_length = 140, required = False)
    secret_answer = forms.CharField(max_length = 100, required = False)

    password = forms.CharField(max_length = 35, required = False)
    password_confirmation = forms.CharField(max_length = 35, required = False)
    
    def clean(self):
        """ Verify password confirmation match. """

        data = super().clean()

        username = data['username']
        secret_question = data['secret_question']
        secret_answer = data['secret_answer']
        try:
            user = User.objects.get(username=username)
        except ObjectDoesNotExist:
            raise forms.ValidationError("El usuario no existe!")
        
        password_retrieval = PasswordRetrieval.objects.get(user=user)
        
        real_secret_question = password_retrieval.secret_question
        real_secret_answer = password_retrieval.secret_answer

        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError("Las contraseñas no coinciden!")

        if secret_question != real_secret_question or secret_answer != real_secret_answer:
            #raise forms.ValidationError({'username': ["Datos de recuperación no validos!",]})
            raise forms.ValidationError("Datos de recuperación no validos!")

        return data