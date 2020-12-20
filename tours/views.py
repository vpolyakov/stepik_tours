from django.http import HttpResponseNotFound, HttpResponseServerError
from django.shortcuts import render
from django.views import View


# Create your views here.


def custom_handler404(request, exception):
    return HttpResponseNotFound('<h1>404<h1><h2>The requested resource was not found on the server.</h2>')


def custom_handler500(request):
    return HttpResponseServerError('<h1>500</h1><h2>That happened internal server error.</h2>')


class MainView(View):

    def get(self, request):
        return render(request, 'index.html')


class DepartureView(View):

    def get(self, request, departure):
        return render(request, 'tours/departure.html')


class TourView(View):

    def get(self, request, id):
        return render(request, 'tours/tour.html')
