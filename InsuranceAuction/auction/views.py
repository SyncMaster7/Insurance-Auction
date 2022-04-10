from django.shortcuts import render
from .models import OtherItem, Vehicle


def home_view(request):
    return render(request, 'auction/home.html')


def vehicles_view(request):
    return render(request, 'auction/vehicles.html')


def all_vehicles(request):
    data_vehicles = Vehicle.object.all()
    context = {
        'others': data_vehicles
    }
    return render(request, 'auction/vehicles.html', context=context)


def motorcycles_view(request):
    return render(request, 'auction/motorcycles.html')


def trailers_view(request):
    return render(request, 'auction/trailers.html')


def parts_view(request):
    return render(request, 'auction/parts.html')


def other_view(request):
    return render(request, 'auction/others.html')


def others(request):
    data_others = OtherItem.object.all()

    context = {
        'others': data_others
    }
    return render(request, 'auction/others.html', context=context)
