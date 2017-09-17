from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from Presentation.forms import FlightCheckForm

# Create your views here.

def index(request):
    form_class = FlightCheckForm
    
    return render(request, 'presentation/index.html', {
        'form': form_class,
    })

def results(request):

    return render(request, 'presentation/results.html', {})