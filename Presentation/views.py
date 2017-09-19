from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from Presentation.forms import FlightCheckForm
from Presentation.models import Results

# Create your views here.

def index(request):
    """ Index page for the app """

    form_class = FlightCheckForm
    
    return render(request, 'presentation/index.html', {
        'form': form_class,
    })

def results(request, flight_number=None, twitter_handle=None):
    """ Captures main form results and displays """

    if request.GET['flight_number'] != '':
        flight_number = request.GET['flight_number']

    if request.GET['twitter_handle'] != '':
        twitter_handle = request.GET['twitter_handle']

    results = Results(flight_number,twitter_handle)

    return render(request, 'presentation/results.html', {
        'results': results,
    })
