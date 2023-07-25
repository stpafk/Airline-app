from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

from .models import Airplane, Airport, Passenger

def index(request):
    return render(request, "flights/index.html", {
        "flights": Airplane.objects.all()
    })

def flight(request, flight_id):
    flight_ = Airplane.objects.get(pk=flight_id)
    return render(request, "flights/flight.html", {
        "flight": flight_,
        "passengers": flight_.passenger.all(),
        "bookings": Passenger.objects.exclude(flights=flight_).all()
    })

def buy(request, flight_id):
    if request.method == "POST":
        flight = Airplane.objects.get(pk=flight_id)
        passenger = Passenger.objects.get(pk=int(request.POST['passenger']))
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse('flight', args=(flight.id,)))