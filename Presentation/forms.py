from django import forms

class FlightCheckForm(forms.Form):
    """ Form schema for main submission """
    flight_number = forms.CharField(required=True, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    twitter_handle = forms.CharField(required=False, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    