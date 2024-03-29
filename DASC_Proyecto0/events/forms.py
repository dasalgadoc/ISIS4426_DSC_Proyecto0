""" Form's module for events app """

# Django

from django import forms

# Models
from .models import Category
from .models import EventType
from .models import Event
from django.contrib.auth.models import User

class EventForm(forms.Form):
    """ Custom form to create or edit events """
    event_pk = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','readonly': None}))
    event_name = forms.CharField(max_length=140,required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    event_site = forms.CharField(max_length=140,required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    event_address = forms.CharField(max_length=200,required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    event_start_date = forms.DateTimeField(widget=forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off', 'id': 'EventIni'}))
    event_end_date = forms.DateTimeField(widget=forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off', 'id': 'EventEnd'}))

    event_category = forms.ModelChoiceField(queryset=Category.objects.all(),empty_label=None, widget=forms.Select(attrs={'class':'form-control'}) )
    event_type = forms.ModelChoiceField(queryset=EventType.objects.all(),empty_label=None, widget=forms.Select(attrs={'class':'form-control'}) )
    event_creator = forms.ModelChoiceField(queryset=User.objects.all(),empty_label=None, widget=forms.Select(attrs={'class':'form-control', 'disabled': None}) )    
    
    def clean(self):
        """ Verify event """
        data = super().clean()
        event_start_date = self.cleaned_data['event_start_date']
        event_end_date = self.cleaned_data['event_end_date']

        if event_start_date > event_end_date:
            raise forms.ValidationError('La fecha de inicio no puede ser mayor que la fecha de fin')

        return data
