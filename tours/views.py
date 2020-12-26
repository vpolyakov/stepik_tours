from random import sample

from django.http import HttpResponse, HttpResponseNotFound, HttpResponseServerError
from django.shortcuts import render
from django.views import View

from tours.data import tours


# Create your views here.

def custom_handler404(request, exception) -> HttpResponse:
    return HttpResponseNotFound('<h1>404<h1><h2>The requested resource was not found on the server.</h2>')


def custom_handler500(request) -> HttpResponse:
    return HttpResponseServerError('<h1>500</h1><h2>That happened internal server error.</h2>')


class MainView(View):

    def get(self, request) -> HttpResponse:
        sample_keys = sample(tours.keys(), k=6)
        tours_sample = {key: value for key, value in tours.items() if key in sample_keys}

        context = {'tours': tours_sample}
        return render(request, 'index.html', context=context)


class DepartureView(View):

    def get(self, request, departure: str) -> HttpResponse:
        d_tours = {key: value for key, value in tours.items() if value["departure"] == departure}

        context = {'tours': d_tours, 'depart_city': departure}
        return render(request, 'tours/departure.html', context=context)


class TourView(View):

    def get(self, request, id: int) -> HttpResponse:

        context = {'tour': tours[id]}
        return render(request, 'tours/tour.html', context=context)
