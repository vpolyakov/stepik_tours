from random import sample

from django.http import HttpResponse, HttpResponseNotFound, HttpResponseServerError
from django.shortcuts import render
from django.views import View

from tours.data import departures, tours

TOUR_NUMBER_MAIN_PAGE = 6


def get_depart_city_runame(depart_dict, city_id) -> str:
    return depart_dict[city_id][0].lower() + depart_dict[city_id][1:]


# Create your views here.

def custom_handler404(request, exception) -> HttpResponse:
    return HttpResponseNotFound('<h1>404<h1><h2>The requested resource was not found on the server.</h2>')


def custom_handler500(request) -> HttpResponse:
    return HttpResponseServerError('<h1>500</h1><h2>That happened internal server error.</h2>')


class MainView(View):

    def get(self, request) -> HttpResponse:
        tour_id_sample = sample(tours.keys(), k=TOUR_NUMBER_MAIN_PAGE)
        tours_sample = {tour_id: tours[tour_id] for tour_id in tour_id_sample}

        context = {'tours': tours_sample}
        return render(request, 'index.html', context=context)


class DepartureView(View):

    def get(self, request, departure: str) -> HttpResponse:

        if departure not in departures.keys():
            return HttpResponseNotFound('<h1>404<h1><h2>Такого места отправления нет!</h2>')

        d_tours = {tour_id: tour for tour_id, tour in tours.items() if tour["departure"] == departure}

        depart_city_ru = get_depart_city_runame(departures, departure)

        context = {'tours': d_tours, 'depart_city': departure, 'depart_city_ru': depart_city_ru}
        return render(request, 'tours/departure.html', context=context)


class TourView(View):

    def get(self, request, id: int) -> HttpResponse:

        if id not in tours.keys():
            return HttpResponseNotFound('<h1>404<h1><h2>Такого тура нет!</h2>')

        tour = tours[id]
        context = {'tour': tour, 'depart_city_ru': get_depart_city_runame(departures, tour['departure'])}
        return render(request, 'tours/tour.html', context=context)
