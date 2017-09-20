from django.shortcuts import render

from Presentation.forms import FlightCheckForm
from Presentation.watcherService import WatcherService


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

    details = WatcherService.watch(twitter_handel=twitter_handle, flight_number=flight_number)

    return render(request, 'presentation/results.html', {
        'vm': details,
    })
