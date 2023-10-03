from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv

from pagination import settings


def index(request):
    return redirect(reverse('bus_stations'))


def get_full_stations():
    with open(settings.BUS_STATION_CSV, encoding='utf-8', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        list_stations = []
        for station in reader:
            list_stations.append({'Name': station['Name'], 'Street': station['Street'], 'District': station['District']})
        return list_stations


CONTENT = get_full_stations()


def bus_stations(request):
    page_number = int(request.GET.get("page", 1))
    paginator = Paginator(CONTENT, 10)
    page = paginator.get_page(page_number)

    context = {
        'bus_stations': [],
        'page': page,
    }

    n = page_number * 10
    for i in range(n - 10, n):
        context['bus_stations'].append(CONTENT[i])

    return render(request, 'stations/index.html', context)
